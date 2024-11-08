def main():
    file_name = input("File name: ").strip().lower()
    media_type(file_name)


def media_type(file_name):
    if not ("." in file_name):
        print("application/octet-stream")
        return

    match file_name.split(".")[-1]:
        case "gif":
            print("image/gif")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "pdf":
            print("application/pdf")
        case "png":
            print("image/png")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")


main()
