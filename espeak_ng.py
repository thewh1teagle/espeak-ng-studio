import subprocess
import os
import signal
from pathlib import Path

class EspeakNG:
    def __init__(self):
        self._espeak_ng = (Path(__file__).parent / "espeak-ng-bin").resolve().absolute()
        self.process = None
        self.env = os.environ.copy()
        if "ESPEAK_DATA_PATH" not in self.env:
            self.env["ESPEAK_DATA_PATH"] = self._espeak_ng.parent / "espeak-ng-data"

    def speak(self, text, voice = 'en'):
        self.process = subprocess.Popen(
            [self._espeak_ng, text, "-v", voice],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            env=self.env
        )
    
    def stop(self):
        """Terminate the espeak process."""
        if self.process and self.process.poll() is None:
            os.kill(self.process.pid, signal.SIGTERM)
            self.process = None
    
    def phonemize(self, text: str, voice: str = 'en') -> str:
        proc = subprocess.Popen([self._espeak_ng, '--ipa', '-v', voice, '-q'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, env=self.env)
        proc.stdin.write(text.encode("utf-8"))
        proc.stdin.close()
        proc.wait()
        return proc.stdout.read().decode("utf-8").strip()
        
    def compile_voice(self, dictsource_path, voice: str = 'en') -> int:
        # ./espeak-ng-bin --compile-phonemes=$(pwd)/espeak-ng/phsource
        # run with shell=True
        proc = subprocess.Popen([self._espeak_ng, f'--compile={voice}'], cwd=dictsource_path, env=self.env)
        return proc.wait()
        