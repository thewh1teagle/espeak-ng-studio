# espeak-ng-studio

Enhance espeak-ng phonemes easily

## Setup

Prepare espeak-ng binary and espeak-ng repository

```console
git clone https://github.com/thewh1teagle/espeak-ng-studio
cd espeak-ng-studio
wget <static espeak-ng>
uv sync
uv run main.py
```

Then prepare [espeak-ng](https://github.com/espeak-ng/espeak-ng)

It's recommended to fork the repository and create new branch for editing. (and finally create [PR](https://github.com/espeak-ng/espeak-ng/pulls) with the edits)

```console
git clone https://github.com/espeak-ng/espeak-ng
cd espeak-ng
code .
```

Now you can edit files in `espeak-ng/dictsource` eg. `espeak-ng/dictsource/en_listx`.

And then enable the `compile` in the browser.


