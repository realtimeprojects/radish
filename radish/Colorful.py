# -*- coding: utf-8 -*-


class Modifiers:
    """ANSI modifiers for Colorful"""
    reset = 0
    bold = 1
    italic = 3
    underline = 4
    blink = 5
    inverse = 7
    strikethrough = 9


class ForeColors:
    """ANSI foreground colors for Colorful"""
    black = 30
    red = 31
    green = 32
    brown = 33
    blue = 34
    magenta = 35
    cyan = 36
    white = 37
    normal = 39


class BackColors:
    """ANSI background colors for Colorful"""
    black = 40
    red = 41
    green = 42
    yellow = 43
    blue = 44
    magenta = 45
    cyan = 46
    white = 47
    normal = 49


class ANSISequenceNotFoundError(Exception):
    """Error if an ANSI sequence could not be found"""
    def __init__(self, modetype, name):
        self.modetype = modetype
        self.name = name

    def __str__(self):
        return "ANSI Sequence `%s` could not be found in `%s`" % (self.name, self.modetype)


class ColorfulParser:
    """Colorful is a class to decorate text with ANSI colors and modifiers."""
    modifiers = Modifiers()
    forecolors = ForeColors()
    backcolors = BackColors()

    modifier_splitter = "and"
    backcolor_splitter = "on"

    @classmethod
    def _IsModifier(cls, modifier):
        return hasattr(cls.modifiers, modifier)

    @classmethod
    def _GetANSIDecorator(cls, mode):
        return "\033[%sm" % (mode)

    @classmethod
    def _TranslateToANSIDecorator(cls, modetype, name):
        if hasattr(modetype, name):
            return cls._GetANSIDecorator(getattr(modetype, name))
        else:
            raise ANSISequenceNotFoundError(modetype.__class__.__name__, name)

    @classmethod
    def ParseAttr(cls, attr):
        parts = attr.split("_")

        modifiers = ""
        forecolor = ""
        backcolor = ""

        if cls._IsModifier(parts[0]):
            modifiers += cls._TranslateToANSIDecorator(cls.modifiers, parts[0])
            parts = parts[1:]

        if cls.modifier_splitter in parts:
            for part in [parts[p + 1] if p + 1 < len(parts) else None for p in range(len(parts)) if parts[p] == cls.modifier_splitter]:
                modifiers += cls._TranslateToANSIDecorator(cls.modifiers, part)
            parts = parts[(len(parts) - parts[-1::-1].index(cls.modifier_splitter) - 1) + 2:]

        if "on" in parts:
            backcolor = cls._TranslateToANSIDecorator(cls.backcolors, parts[parts.index(cls.backcolor_splitter) + 1])
            parts = parts[:-2]

        if len(parts) > 0:
            forecolor = cls._TranslateToANSIDecorator(cls.forecolors, parts[0])

        return modifiers + forecolor + backcolor + "%s" + cls._TranslateToANSIDecorator(cls.modifiers, "reset")


class ColorfulMeta(type):
    class ColorfulOut(type):
        def __getattr__(cls, attr):
            def decoratedText(text):
                print(ColorfulParser.ParseAttr(attr) % (text))
            return decoratedText

    out = ColorfulOut("out", (object, ), {})

    def __getattr__(cls, attr):
        def decoratedText(text):
            return ColorfulParser.ParseAttr(attr) % (text)
        return decoratedText

colorful = ColorfulMeta("cf", (object, ), {})
