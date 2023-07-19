from dl_translate import lang
from .logger import logger


class Dict(dict):
    def __missing__(self, key):
        logger.warning(
            f"Cannot find {key} in Constants.LANGUAGES, "
            "returning the original string ..."
        )
        return key


class Constants:
    # Some constant values.
    BATCH = 16  # reduce if low on GPU mem
    COMPUTE_TYPE = "float16"
    LANGUAGES = Dict({
        "en": lang.ENGLISH,
        "zh": lang.nllb200.CHINESE_SIMPLIFIED,
        "zh_CN": lang.nllb200.CHINESE_SIMPLIFIED,
        "zh_Hans": lang.nllb200.CHINESE_SIMPLIFIED,
        "zh_TW": lang.nllb200.CHINESE_TRADITIONAL,
        "zh_HK": lang.nllb200.CHINESE_TRADITIONAL,
        "zh_Hant": lang.nllb200.CHINESE_TRADITIONAL,
        "de": lang.GERMAN,
        "es": lang.SPANISH,
        "ru": lang.RUSSIAN,
        "ko": lang.KOREAN,
        "fr": lang.FRENCH,
        "ja": lang.JAPANESE,
        "pt": lang.PORTUGUESE,
        "tr": lang.TURKISH,
        "pl": lang.POLISH,
        "ca": lang.CATALAN,
        "nl": lang.DUTCH,
        "ar": lang.ARABIC,
        "sv": lang.SWEDISH,
        "it": lang.ITALIAN,
        "id": lang.INDONESIAN,
        "hi": lang.HINDI,
        "fi": lang.FINNISH,
        "vi": lang.VIETNAMESE,
        "he": lang.HEBREW,
        "uk": lang.UKRAINIAN,
        "el": lang.GREEK,
        "ms": lang.MALAY,
        "cs": lang.CZECH,
        "ro": lang.ROMANIAN,
        "da": lang.DANISH,
        "hu": lang.HUNGARIAN,
        "ta": lang.TAMIL,
        "no": lang.NORWEGIAN,
        "th": lang.THAI,
        "ur": lang.URDU,
        "hr": lang.CROATIAN,
        "bg": lang.BULGARIAN,
        "lt": lang.LITHUANIAN,
        "ml": lang.MALAYALAM,
        "cy": lang.WELSH,
        "sk": lang.SLOVAK,
        "fa": lang.PERSIAN,
        "lv": lang.LATVIAN,
        "bn": lang.BENGALI,
        "sr": lang.SERBIAN,
        "az": lang.AZERBAIJANI,
        "sl": lang.SLOVENIAN,
        "kn": lang.KANNADA,
        "et": lang.ESTONIAN,
        "br": lang.BRETON,
        "is": lang.ICELANDIC,
        "hy": lang.ARMENIAN,
        "ne": lang.NEPALI,
        "mn": lang.MONGOLIAN,
        "bs": lang.BOSNIAN,
        "kk": lang.KAZAKH,
        "sq": lang.ALBANIAN,
        "sw": lang.SWAHILI,
        "gl": lang.GALICIAN,
        "mr": lang.MARATHI,
        "pa": lang.PUNJABI,
        "si": lang.SINHALA,
        "km": lang.KHMER,
        "yo": lang.YORUBA,
        "so": lang.SOMALI,
        "af": lang.AFRIKAANS,
        "oc": lang.OCCITAN,
        "ka": lang.GEORGIAN,
        "be": lang.BELARUSIAN,
        "sd": lang.SINDHI,
        "gu": lang.GUJARATI,
        "am": lang.AMHARIC,
        "yi": lang.YIDDISH,
        "lo": lang.LAO,
        "uz": lang.UZBEK,
        "ht": lang.HAITIAN_CREOLE,
        "ps": lang.PASHTO,
        "lb": lang.LUXEMBOURGISH,
        "tl": lang.TAGALOG,
        "mg": lang.MALAGASY,
        "ln": lang.LINGALA,
        "ha": lang.HAUSA,
        "ba": lang.BASHKIR,
        "jw": lang.JAVANESE,
        "su": lang.SUNDANESE,
    })
