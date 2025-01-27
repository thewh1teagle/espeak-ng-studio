import subprocess
import os
import signal
from pathlib import Path
import platform
import stat
import tempfile
import random
import string

class EspeakNG:
    def __init__(self):
        self._espeak_ng = (Path(__file__).parent / "espeak-ng-bin").resolve().absolute()
        self.temp_path = Path(tempfile.gettempdir()) / ''.join(random.choices(string.ascii_letters, k=10))
        if not self._espeak_ng.exists():
            raise FileNotFoundError(f'Cannot find espeak-ng-bin at {self._espeak_ng}')
        if platform.system() != 'Windows':
            st = os.stat(self._espeak_ng)
            os.chmod(self._espeak_ng, st.st_mode | stat.S_IEXEC)
            
        self.process = None
        self.env = os.environ.copy()
        if "ESPEAK_DATA_PATH" not in self.env:
            self.env["ESPEAK_DATA_PATH"] = self._espeak_ng.parent / "espeak-ng"

    def speak(self, text, voice='en', rate=175):
        self.process = subprocess.Popen(
            [self._espeak_ng, text, "-v", voice, "-s", str(rate)],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            env=self.env
        )

    
    def stop(self):
        """Terminate the espeak process."""
        if self.process and self.process.poll() is None:
            os.kill(self.process.pid, signal.SIGTERM)
            self.process = None
    
    def phonemize(self, text: str, voice: str = 'en') -> str:
        with open(self.temp_path, 'w') as f:
            f.write(text)
        cmd = [str(self._espeak_ng), '--ipa', '-v', voice, '-q', '-f', str(self.temp_path)]
        # print(' '.join(cmd))
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, env=self.env)
        proc.stdin.write(text.encode("utf-8"))
        proc.stdin.close()
        proc.wait()
        return proc.stdout.read().decode("utf-8").strip()
        
    def _compile_phonemes(self):
        proc = subprocess.Popen([self._espeak_ng, f'--compile-phonemes'], env=self.env)
        return proc.wait()
    
    def _compile_intonations(self):
        proc = subprocess.Popen([self._espeak_ng, f'--compile-intonations'], env=self.env)
        return proc.wait()
        
    def compile_voice(self, dictsource_path, voice: str = 'en') -> int:
        # ./espeak-ng-bin --compile-phonemes=$(pwd)/espeak-ng/phsource
        self._compile_phonemes()
        self._compile_intonations()
        proc = subprocess.Popen([self._espeak_ng, f'--compile={voice}'], cwd=dictsource_path, env=self.env)
        return proc.wait()
        