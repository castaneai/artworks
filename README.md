# artworks
Python library getting artwork image from audio

## Requirements

- Python 3.6+

## Install

```sh
pip install artworks
```

## Usage

```python
import artworks

aw = artworks.from_file('/path/to/audio_file.mp3')
print(aw.mime_type)
print(aw.data_bytes[:20])
```

## Supported file types

- MP3
- MP4