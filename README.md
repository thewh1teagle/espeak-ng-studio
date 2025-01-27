# espeak-ng-studio

Enhance espeak-ng phonemes easily

<img src="https://github.com/user-attachments/assets/c6dfbc10-8cb1-4b8b-8e6c-9f78e7e186b0" width=600>

## Setup

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) (Python)


Prepare the studio

```console
git clone https://github.com/thewh1teagle/espeak-ng-studio
cd espeak-ng-studio
uv sync
```

Prepare espeak-ng repository

It's recommended to fork the repository and create new branch for editing. (and finally create [PR](https://github.com/espeak-ng/espeak-ng/pulls) with the edits)

```console
git clone https://github.com/espeak-ng/espeak-ng
cd espeak-ng
code .
```

Prepare espeak-ng binary in the studio

Windows PowerShell

```console
winget install -e --id JernejSimoncic.Wget
wget.exe https://github.com/thewh1teagle/espeak-ng-static/releases/download/v1.52/espeak-ng-static-windows-amd64.exe -O espeak-ng-bin.exe
```

Linux

```
sudo apt install -y pcaudiolib wget
wget https://github.com/thewh1teagle/espeak-ng-static/releases/download/v1.52/espeak-ng-static-linux-amd64 -O espeak-ng-bin
chmod +x espeak-ng-bin
```

macOS

```console
wget https://github.com/thewh1teagle/espeak-ng-static/releases/download/v1.52/espeak-ng-static-macos-universal -O espeak-ng-bin
chmod +x espeak-ng-bin
```

Run

```console
uv run main.py
```

Now you can edit files in `espeak-ng/dictsource` eg. `espeak-ng/dictsource/en_listx`.

And then enable the `compile` in the browser.


