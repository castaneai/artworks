import artworks


def test_mp4():
    aw = artworks.from_file('sample.m4a')
    assert isinstance(aw, artworks.Artwork)
    assert aw.mime_type == 'image/jpeg'


def test_mp3():
    aw = artworks.from_file('sample.mp3')
    assert isinstance(aw, artworks.Artwork)
    assert aw.mime_type == 'image/jpeg'
