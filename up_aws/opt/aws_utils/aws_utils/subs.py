def subs():
    print("*** Generating Subtitles using AWS ***")
    print("* Validate credentials (sts get client identity)")
    print("* Find files to translate (python glob)")
    print("* Find or create data bucket (aws s3)")
    print("* Upload videos to bucket (aws s3)")
    print("* Start and wait transcribe job")
    print("* Start and wait translate job")
    print("* Download translated subtitles")
    print("* ...")

#main invoke
if __name__ == "__main__":
    main()