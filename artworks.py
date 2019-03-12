import mutagen
import mutagen.mp3
import mutagen.mp4
import mutagen.id3
import mutagen.easyid3
import mutagen.easymp4

_SUPPORTED_MUTAGEN_FILE_TYPES = (
    mutagen.mp3.EasyMP3,
    mutagen.easymp4.EasyMP4,
)


def _id3tags_to_artwork(id3tags, _):
    tag = next((pic for pic in id3tags.getall('APIC') if pic.type == mutagen.id3.PictureType.COVER_FRONT), None)
    if not isinstance(tag, mutagen.id3.APIC):
        return None
    return Artwork(tag.mime, tag.data)


def _mp4tags_to_artwork(mp4tags, _):
    tag = mp4tags.get("covr", None)
    if not isinstance(tag, list) or len(tag) < 1:
        return None
    c = tag[0]
    if not isinstance(c, mutagen.mp4.MP4Cover):
        return None
    return Artwork(_mp4_cover_to_mime_type(c), bytes(c))


def _mp4_cover_to_mime_type(mp4_cover):
    return {
        mutagen.mp4.MP4Cover.FORMAT_JPEG: "image/jpeg",
        mutagen.mp4.MP4Cover.FORMAT_PNG: "image/png",
    }.get(mp4_cover.imageformat, None)


def _get_mime_type(mutagen_file: mutagen.FileType):
    if len(mutagen_file.mime) > 0:
        return mutagen_file.mime[0]
    raise Exception("mime/type not found: " + mutagen_file.filename)


mutagen.easyid3.EasyID3.RegisterKey("artwork", _id3tags_to_artwork)
mutagen.easymp4.EasyMP4.RegisterKey("artwork", _mp4tags_to_artwork)


class Artwork:

    def __init__(self, mime_type, data_bytes):
        self.mime_type = mime_type
        self.data_bytes = data_bytes


def from_file(file) -> Artwork:
    return mutagen.File(file, easy=True).get("artwork", None)
