#!/usr/bin/env python3

"""
Program prompts the user for the name of a file and then outputs that file’s
media type if the file’s name ends, case-insensitively, in any of these
suffixes:

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip

"""


def extension(filename: str) -> str:
    """
    Determine the file extension of a given file.

    Arguments:
        filename: The name of the file.

    Returns:
        str
            The file extension.
    """

    extension = filename.split(".")

    return f".{extension[-1].lower()}"


def file_type(extension: str, mime_type: dict[str, list[str]]) -> str:
    """
    Determine the media type of a given file extension. If the file extension
    is not found in the dictionary, the media type is set to
    "application/octet-stream".

    If the file extension is found in the dictionary, the media type is set to
    the key of the dictionary and the file extension, stripping the period from
    the extension.

    Arguments:
        extension: The file extension.
        mime_type: A dictionary containing the media types.

    Returns:
        str
            The media type of the file.
    """

    for key, value in mime_type.items():
        if extension.endswith(".jpg") or extension.endswith(".jpeg"):
            return f"{key}/jpeg"
        if extension.endswith(".txt"):
            return f"text/plain"
        elif extension in value:
            return f"{key}/{extension[1:]}"
    else:
        return "application/octet-stream"

mime_types = {
    "image": [
        ".gif",
        ".jpg",
        ".jpeg",
        ".png"
        ],
    "application": [
        ".pdf",
        ".zip"
        ],
    "text": [
        ".txt"
        ]
    }

def main() -> None:
    """
    Prompt the user for the name of a file and then output that file’s media
    type.
    """

    filename = input("File name: ").strip()

    ext = extension(filename)

    print(file_type(ext, mime_types))


if __name__ == "__main__":
    main()
