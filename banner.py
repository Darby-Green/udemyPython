def bannerText(text: str = " ", screenWidth: int = 80) -> None:
    """
    Print a string centered, with `**` on either side.
    :param text: The string to print
    an `*` will print a row of `*` to the desired `screenWidth`
    :param screenWidth: Overall width to print in
    :Raises ValueError: if the passed string is longer than the screenWidth
    peram
    :return:
    """
    if len(text) > screenWidth - 4:
        raise ValueError("String '{0}' is larger than the specified width!! {1}"
                         .format(text, screenWidth))

    if text == "*":
        print("*" * screenWidth)
    else:
        outputString = "**{0}**".format(text.center(screenWidth - 4))
        print(outputString)


bannerText("*")
bannerText("Always look on the bright side of life...")
bannerText("If life seems jolly rotten,")
bannerText("There's something you've forgotten!")
bannerText("And that's to laugh and smile and dance and sing,")
bannerText(" ")
bannerText("When your feeling in the dumps,")
bannerText("Don't be silly chumps,")
bannerText("Just purse your lips and whistle = that's the thing!")
bannerText("And... always look on the bright side of life...")
bannerText("*")
