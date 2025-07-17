Media_type=input("Enter the media name").strip().lower()
if Media_type.endswith(".jpg"):
    print("image/jpg")
elif Media_type.endswith(".pdf"):
    print("document/pdf")
elif Media_type.endswith(".docx"):
    print("document/docx")
elif Media_type.endswith(".txt"):
    print("text/txt")
elif Media_type.endswith(".png"):
    print("image/png")
elif Media_type.endswith(".zip"):
    print("application/zip")
elif Media_type.endswith(".jpeg"):
    print("image/jpeg")
elif Media_type.endswith(".gif"):
    print("image/gif")
else:
    print("application/octet-stream")
# The code checks the file extension of a media file and prints its MIME type.
