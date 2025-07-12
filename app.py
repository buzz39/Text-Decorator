# -*- coding: utf-8 -*-
"""
Complete Unicode Text Styling System
Handles letters, digits, and combining marks with proper code point mapping
"""

import unicodedata
from itertools import chain

# ========================
# UNICODE CONFIGURATION
# ========================
# Unicode character mappings for different styles
STYLE_CONFIG = {
    'bold': {
        'A': '𝐀', 'B': '𝐁', 'C': '𝐂', 'D': '𝐃', 'E': '𝐄', 'F': '𝐅', 'G': '𝐆', 'H': '𝐇', 'I': '𝐈', 'J': '𝐉',
        'K': '𝐊', 'L': '𝐋', 'M': '𝐌', 'N': '𝐍', 'O': '𝐎', 'P': '𝐏', 'Q': '𝐐', 'R': '𝐑', 'S': '𝐒', 'T': '𝐓',
        'U': '𝐔', 'V': '𝐕', 'W': '𝐖', 'X': '𝐗', 'Y': '𝐘', 'Z': '𝐙',
        'a': '𝐚', 'b': '𝐛', 'c': '𝐜', 'd': '𝐝', 'e': '𝐞', 'f': '𝐟', 'g': '𝐠', 'h': '𝐡', 'i': '𝐢', 'j': '𝐣',
        'k': '𝐤', 'l': '𝐥', 'm': '𝐦', 'n': '𝐧', 'o': '𝐨', 'p': '𝐩', 'q': '𝐪', 'r': '𝐫', 's': '𝐬', 't': '𝐭',
        'u': '𝐮', 'v': '𝐯', 'w': '𝐰', 'x': '𝐱', 'y': '𝐲', 'z': '𝐳',
        '0': '𝟎', '1': '𝟏', '2': '𝟐', '3': '𝟑', '4': '𝟒', '5': '𝟓', '6': '𝟔', '7': '𝟕', '8': '𝟖', '9': '𝟗'
    },
    'italic': {
        'A': '𝐴', 'B': '𝐵', 'C': '𝐶', 'D': '𝐷', 'E': '𝐸', 'F': '𝐹', 'G': '𝐺', 'H': '𝐻', 'I': '𝐼', 'J': '𝐽',
        'K': '𝐾', 'L': '𝐿', 'M': '𝑀', 'N': '𝑁', 'O': '𝑂', 'P': '𝑃', 'Q': '𝑄', 'R': '𝑅', 'S': '𝑆', 'T': '𝑇',
        'U': '𝑈', 'V': '𝑉', 'W': '𝑊', 'X': '𝑋', 'Y': '𝑌', 'Z': '𝑍',
        'a': '𝑎', 'b': '𝑏', 'c': '𝑐', 'd': '𝑑', 'e': '𝑒', 'f': '𝑓', 'g': '𝑔', 'h': 'ℎ', 'i': '𝑖', 'j': '𝑗',
        'k': '𝑘', 'l': '𝑙', 'm': '𝑚', 'n': '𝑛', 'o': '𝑜', 'p': '𝑝', 'q': '𝑞', 'r': '𝑟', 's': '𝑠', 't': '𝑡',
        'u': '𝑢', 'v': '𝑣', 'w': '𝑤', 'x': '𝑥', 'y': '𝑦', 'z': '𝑧'
    },
    'bold_italic': {
        'A': '𝑨', 'B': '𝑩', 'C': '𝑪', 'D': '𝑫', 'E': '𝑬', 'F': '𝑭', 'G': '𝑮', 'H': '𝑯', 'I': '𝑰', 'J': '𝑱',
        'K': '𝑲', 'L': '𝑳', 'M': '𝑴', 'N': '𝑵', 'O': '𝑶', 'P': '𝑷', 'Q': '𝑸', 'R': '𝑹', 'S': '𝑺', 'T': '𝑻',
        'U': '𝑼', 'V': '𝑽', 'W': '𝑾', 'X': '𝑿', 'Y': '𝒀', 'Z': '𝒁',
        'a': '𝒂', 'b': '𝒃', 'c': '𝒄', 'd': '𝒅', 'e': '𝒆', 'f': '𝒇', 'g': '𝒈', 'h': '𝒉', 'i': '𝒊', 'j': '𝒋',
        'k': '𝒌', 'l': '𝒍', 'm': '𝒎', 'n': '𝒏', 'o': '𝒐', 'p': '𝒑', 'q': '𝒒', 'r': '𝒓', 's': '𝒔', 't': '𝒕',
        'u': '𝒖', 'v': '𝒗', 'w': '𝒘', 'x': '𝒙', 'y': '𝒚', 'z': '𝒛'
    },
    'script': {
        'A': '𝒜', 'B': 'ℬ', 'C': '𝒞', 'D': '𝒟', 'E': 'ℰ', 'F': 'ℱ', 'G': '𝒢', 'H': 'ℋ', 'I': 'ℐ', 'J': '𝒥',
        'K': '𝒦', 'L': 'ℒ', 'M': 'ℳ', 'N': '𝒩', 'O': '𝒪', 'P': '𝒫', 'Q': '𝒬', 'R': 'ℛ', 'S': '𝒮', 'T': '𝒯',
        'U': '𝒰', 'V': '𝒱', 'W': '𝒲', 'X': '𝒳', 'Y': '𝒴', 'Z': '𝒵',
        'a': '𝒶', 'b': '𝒷', 'c': '𝒸', 'd': '𝒹', 'e': 'ℯ', 'f': '𝒻', 'g': 'ℊ', 'h': '𝒽', 'i': '𝒾', 'j': '𝒿',
        'k': '𝓀', 'l': '𝓁', 'm': '𝓂', 'n': '𝓃', 'o': 'ℴ', 'p': '𝓅', 'q': '𝓆', 'r': '𝓇', 's': '𝓈', 't': '𝓉',
        'u': '𝓊', 'v': '𝓋', 'w': '𝓌', 'x': '𝓍', 'y': '𝓎', 'z': '𝓏'
    },
    'bold_script': {
        'A': '𝓐', 'B': '𝓑', 'C': '𝓒', 'D': '𝓓', 'E': '𝓔', 'F': '𝓕', 'G': '𝓖', 'H': '𝓗', 'I': '𝓘', 'J': '𝓙',
        'K': '𝓚', 'L': '𝓛', 'M': '𝓜', 'N': '𝓝', 'O': '𝓞', 'P': '𝓟', 'Q': '𝓠', 'R': '𝓡', 'S': '𝓢', 'T': '𝓣',
        'U': '𝓤', 'V': '𝓥', 'W': '𝓦', 'X': '𝓧', 'Y': '𝓨', 'Z': '𝓩',
        'a': '𝓪', 'b': '𝓫', 'c': '𝓬', 'd': '𝓭', 'e': '𝓮', 'f': '𝓯', 'g': '𝓰', 'h': '𝓱', 'i': '𝓲', 'j': '𝓳',
        'k': '𝓴', 'l': '𝓵', 'm': '𝓶', 'n': '𝓷', 'o': '𝓸', 'p': '𝓹', 'q': '𝓺', 'r': '𝓻', 's': '𝓼', 't': '𝓽',
        'u': '𝓾', 'v': '𝓿', 'w': '𝔀', 'x': '𝔁', 'y': '𝔂', 'z': '𝔃'
    },
    'fraktur': {
        'A': '𝔄', 'B': '𝔅', 'C': 'ℭ', 'D': '𝔇', 'E': '𝔈', 'F': '𝔉', 'G': '𝔊', 'H': 'ℌ', 'I': 'ℑ', 'J': '𝔍',
        'K': '𝔎', 'L': '𝔏', 'M': '𝔐', 'N': '𝔑', 'O': '𝔒', 'P': '𝔓', 'Q': '𝔔', 'R': 'ℜ', 'S': '𝔖', 'T': '𝔗',
        'U': '𝔘', 'V': '𝔙', 'W': '𝔚', 'X': '𝔛', 'Y': '𝔜', 'Z': 'ℨ',
        'a': '𝔞', 'b': '𝔟', 'c': '𝔠', 'd': '𝔡', 'e': '𝔢', 'f': '𝔣', 'g': '𝔤', 'h': '𝔥', 'i': '𝔦', 'j': '𝔧',
        'k': '𝔨', 'l': '𝔩', 'm': '𝔪', 'n': '𝔫', 'o': '𝔬', 'p': '𝔭', 'q': '𝔮', 'r': '𝔯', 's': '𝔰', 't': '𝔱',
        'u': '𝔲', 'v': '𝔳', 'w': '𝔴', 'x': '𝔵', 'y': '𝔶', 'z': '𝔷'
    },
    'double_struck': {
        'A': '𝔸', 'B': '𝔹', 'C': 'ℂ', 'D': '𝔻', 'E': '𝔼', 'F': '𝔽', 'G': '𝔾', 'H': 'ℍ', 'I': '𝕀', 'J': '𝕁',
        'K': '𝕂', 'L': '𝕃', 'M': '𝕄', 'N': 'ℕ', 'O': '𝕆', 'P': 'ℙ', 'Q': 'ℚ', 'R': 'ℝ', 'S': '𝕊', 'T': '𝕋',
        'U': '𝕌', 'V': '𝕍', 'W': '𝕎', 'X': '𝕏', 'Y': '𝕐', 'Z': 'ℤ',
        'a': '𝕒', 'b': '𝕓', 'c': '𝕔', 'd': '𝕕', 'e': '𝕖', 'f': '𝕗', 'g': '𝕘', 'h': '𝕙', 'i': '𝕚', 'j': '𝕛',
        'k': '𝕜', 'l': '𝕝', 'm': '𝕞', 'n': '𝕟', 'o': '𝕠', 'p': '𝕡', 'q': '𝕢', 'r': '𝕣', 's': '𝕤', 't': '𝕥',
        'u': '𝕦', 'v': '𝕧', 'w': '𝕨', 'x': '𝕩', 'y': '𝕪', 'z': '𝕫',
        '0': '𝟘', '1': '𝟙', '2': '𝟚', '3': '𝟛', '4': '𝟜', '5': '𝟝', '6': '𝟞', '7': '𝟟', '8': '𝟠', '9': '𝟡'
    },
    'sans_serif': {
        'A': '𝖠', 'B': '𝖡', 'C': '𝖢', 'D': '𝖣', 'E': '𝖤', 'F': '𝖥', 'G': '𝖦', 'H': '𝖧', 'I': '𝖨', 'J': '𝖩',
        'K': '𝖪', 'L': '𝖫', 'M': '𝖬', 'N': '𝖭', 'O': '𝖮', 'P': '𝖯', 'Q': '𝖰', 'R': '𝖱', 'S': '𝖲', 'T': '𝖳',
        'U': '𝖴', 'V': '𝖵', 'W': '𝖶', 'X': '𝖷', 'Y': '𝖸', 'Z': '𝖹',
        'a': '𝖺', 'b': '𝖻', 'c': '𝖼', 'd': '𝖽', 'e': '𝖾', 'f': '𝖿', 'g': '𝗀', 'h': '𝗁', 'i': '𝗂', 'j': '𝗃',
        'k': '𝗄', 'l': '𝗅', 'm': '𝗆', 'n': '𝗇', 'o': '𝗈', 'p': '𝗉', 'q': '𝗊', 'r': '𝗋', 's': '𝗌', 't': '𝗍',
        'u': '𝗎', 'v': '𝗏', 'w': '𝗐', 'x': '𝗑', 'y': '𝗒', 'z': '𝗓',
        '0': '𝟢', '1': '𝟣', '2': '𝟤', '3': '𝟥', '4': '𝟦', '5': '𝟧', '6': '𝟨', '7': '𝟩', '8': '𝟪', '9': '𝟫'
    },
    'sans_bold': {
        'A': '𝗔', 'B': '𝗕', 'C': '𝗖', 'D': '𝗗', 'E': '𝗘', 'F': '𝗙', 'G': '𝗚', 'H': '𝗛', 'I': '𝗜', 'J': '𝗝',
        'K': '𝗞', 'L': '𝗟', 'M': '𝗠', 'N': '𝗡', 'O': '𝗢', 'P': '𝗣', 'Q': '𝗤', 'R': '𝗥', 'S': '𝗦', 'T': '𝗧',
        'U': '𝗨', 'V': '𝗩', 'W': '𝗪', 'X': '𝗫', 'Y': '𝗬', 'Z': '𝗭',
        'a': '𝗮', 'b': '𝗯', 'c': '𝗰', 'd': '𝗱', 'e': '𝗲', 'f': '𝗳', 'g': '𝗴', 'h': '𝗵', 'i': '𝗶', 'j': '𝗷',
        'k': '𝗸', 'l': '𝗹', 'm': '𝗺', 'n': '𝗻', 'o': '𝗼', 'p': '𝗽', 'q': '𝗾', 'r': '𝗿', 's': '𝘀', 't': '𝘁',
        'u': '𝘂', 'v': '𝘃', 'w': '𝘄', 'x': '𝘅', 'y': '𝘆', 'z': '𝘇',
        '0': '𝟬', '1': '𝟭', '2': '𝟮', '3': '𝟯', '4': '𝟰', '5': '𝟱', '6': '𝟲', '7': '𝟳', '8': '𝟴', '9': '𝟵'
    },
    'sans_italic': {
        'A': '𝘈', 'B': '𝘉', 'C': '𝘊', 'D': '𝘋', 'E': '𝘌', 'F': '𝘍', 'G': '𝘎', 'H': '𝘏', 'I': '𝘐', 'J': '𝘑',
        'K': '𝘒', 'L': '𝘓', 'M': '𝘔', 'N': '𝘕', 'O': '𝘖', 'P': '𝘗', 'Q': '𝘘', 'R': '𝘙', 'S': '𝘚', 'T': '𝘛',
        'U': '𝘜', 'V': '𝘝', 'W': '𝘞', 'X': '𝘟', 'Y': '𝘠', 'Z': '𝘡',
        'a': '𝘢', 'b': '𝘣', 'c': '𝘤', 'd': '𝘥', 'e': '𝘦', 'f': '𝘧', 'g': '𝘨', 'h': '𝘩', 'i': '𝘪', 'j': '𝘫',
        'k': '𝘬', 'l': '𝘭', 'm': '𝘮', 'n': '𝘯', 'o': '𝘰', 'p': '𝘱', 'q': '𝘲', 'r': '𝘳', 's': '𝘴', 't': '𝘵',
        'u': '𝘶', 'v': '𝘷', 'w': '𝘸', 'x': '𝘹', 'y': '𝘺', 'z': '𝘻'
    },
    'sans_bold_italic': {
        'A': '𝘼', 'B': '𝘽', 'C': '𝘾', 'D': '𝘿', 'E': '𝙀', 'F': '𝙁', 'G': '𝙂', 'H': '𝙃', 'I': '𝙄', 'J': '𝙅',
        'K': '𝙆', 'L': '𝙇', 'M': '𝙈', 'N': '𝙉', 'O': '𝙊', 'P': '𝙋', 'Q': '𝙌', 'R': '𝙍', 'S': '𝙎', 'T': '𝙏',
        'U': '𝙐', 'V': '𝙑', 'W': '𝙒', 'X': '𝙓', 'Y': '𝙔', 'Z': '𝙕',
        'a': '𝙖', 'b': '𝙗', 'c': '𝙘', 'd': '𝙙', 'e': '𝙚', 'f': '𝙛', 'g': '𝙜', 'h': '𝙝', 'i': '𝙞', 'j': '𝙟',
        'k': '𝙠', 'l': '𝙡', 'm': '𝙢', 'n': '𝙣', 'o': '𝙤', 'p': '𝙥', 'q': '𝙦', 'r': '𝙧', 's': '𝙨', 't': '𝙩',
        'u': '𝙪', 'v': '𝙫', 'w': '𝙬', 'x': '𝙭', 'y': '𝙮', 'z': '𝙯'
    },
    'monospace': {
        'A': '𝙰', 'B': '𝙱', 'C': '𝙲', 'D': '𝙳', 'E': '𝙴', 'F': '𝙵', 'G': '𝙶', 'H': '𝙷', 'I': '𝙸', 'J': '𝙹',
        'K': '𝙺', 'L': '𝙻', 'M': '𝙼', 'N': '𝙽', 'O': '𝙾', 'P': '𝙿', 'Q': '𝚀', 'R': '𝚁', 'S': '𝚂', 'T': '𝚃',
        'U': '𝚄', 'V': '𝚅', 'W': '𝚆', 'X': '𝚇', 'Y': '𝚈', 'Z': '𝚉',
        'a': '𝚊', 'b': '𝚋', 'c': '𝚌', 'd': '𝚍', 'e': '𝚎', 'f': '𝚏', 'g': '𝚐', 'h': '𝚑', 'i': '𝚒', 'j': '𝚓',
        'k': '𝚔', 'l': '𝚕', 'm': '𝚖', 'n': '𝚗', 'o': '𝚘', 'p': '𝚙', 'q': '𝚚', 'r': '𝚛', 's': '𝚜', 't': '𝚝',
        'u': '𝚞', 'v': '𝚟', 'w': '𝚠', 'x': '𝚡', 'y': '𝚢', 'z': '𝚣',
        '0': '𝟶', '1': '𝟷', '2': '𝟸', '3': '𝟹', '4': '𝟺', '5': '𝟻', '6': '𝟼', '7': '𝟽', '8': '𝟾', '9': '𝟿'
    },
    # Missing Mathematical Alphanumeric Symbols
    'bold_fraktur': {
        'A': '𝕬', 'B': '𝕭', 'C': '𝕮', 'D': '𝕯', 'E': '𝕰', 'F': '𝕱', 'G': '𝕲', 'H': '𝕳', 'I': '𝕴', 'J': '𝕵',
        'K': '𝕶', 'L': '𝕷', 'M': '𝕸', 'N': '𝕹', 'O': '𝕺', 'P': '𝕻', 'Q': '𝕼', 'R': '𝕽', 'S': '𝕾', 'T': '𝕿',
        'U': '𝖀', 'V': '𝖁', 'W': '𝖂', 'X': '𝖃', 'Y': '𝖄', 'Z': '𝖅',
        'a': '𝖆', 'b': '𝖇', 'c': '𝖈', 'd': '𝖉', 'e': '𝖊', 'f': '𝖋', 'g': '𝖌', 'h': '𝖍', 'i': '𝖎', 'j': '𝖏',
        'k': '𝖐', 'l': '𝖑', 'm': '𝖒', 'n': '𝖓', 'o': '𝖔', 'p': '𝖕', 'q': '𝖖', 'r': '𝖗', 's': '𝖘', 't': '𝖙',
        'u': '𝖚', 'v': '𝖛', 'w': '𝖜', 'x': '𝖝', 'y': '𝖞', 'z': '𝖟'
    },
    # Fullwidth/Vaporwave styles
    'fullwidth': {
        'A': 'Ａ', 'B': 'Ｂ', 'C': 'Ｃ', 'D': 'Ｄ', 'E': 'Ｅ', 'F': 'Ｆ', 'G': 'Ｇ', 'H': 'Ｈ', 'I': 'Ｉ', 'J': 'Ｊ',
        'K': 'Ｋ', 'L': 'Ｌ', 'M': 'Ｍ', 'N': 'Ｎ', 'O': 'Ｏ', 'P': 'Ｐ', 'Q': 'Ｑ', 'R': 'Ｒ', 'S': 'Ｓ', 'T': 'Ｔ',
        'U': 'Ｕ', 'V': 'Ｖ', 'W': 'Ｗ', 'X': 'Ｘ', 'Y': 'Ｙ', 'Z': 'Ｚ',
        'a': 'ａ', 'b': 'ｂ', 'c': 'ｃ', 'd': 'ｄ', 'e': 'ｅ', 'f': 'ｆ', 'g': 'ｇ', 'h': 'ｈ', 'i': 'ｉ', 'j': 'ｊ',
        'k': 'ｋ', 'l': 'ｌ', 'm': 'ｍ', 'n': 'ｎ', 'o': 'ｏ', 'p': 'ｐ', 'q': 'ｑ', 'r': 'ｒ', 's': 'ｓ', 't': 'ｔ',
        'u': 'ｕ', 'v': 'ｖ', 'w': 'ｗ', 'x': 'ｘ', 'y': 'ｙ', 'z': 'ｚ',
        '0': '０', '1': '１', '2': '２', '3': '３', '4': '４', '5': '５', '6': '６', '7': '７', '8': '８', '9': '９',
        ' ': '　'  # Fullwidth space
    },
    # Small caps style
    'small_caps': {
        'A': 'ᴀ', 'B': 'ʙ', 'C': 'ᴄ', 'D': 'ᴅ', 'E': 'ᴇ', 'F': 'ꜰ', 'G': 'ɢ', 'H': 'ʜ', 'I': 'ɪ', 'J': 'ᴊ',
        'K': 'ᴋ', 'L': 'ʟ', 'M': 'ᴍ', 'N': 'ɴ', 'O': 'ᴏ', 'P': 'ᴘ', 'Q': 'Q', 'R': 'ʀ', 'S': 'ꜱ', 'T': 'ᴛ',
        'U': 'ᴜ', 'V': 'ᴠ', 'W': 'ᴡ', 'X': 'x', 'Y': 'ʏ', 'Z': 'ᴢ',
        'a': 'ᴀ', 'b': 'ʙ', 'c': 'ᴄ', 'd': 'ᴅ', 'e': 'ᴇ', 'f': 'ꜰ', 'g': 'ɢ', 'h': 'ʜ', 'i': 'ɪ', 'j': 'ᴊ',
        'k': 'ᴋ', 'l': 'ʟ', 'm': 'ᴍ', 'n': 'ɴ', 'o': 'ᴏ', 'p': 'ᴘ', 'q': 'q', 'r': 'ʀ', 's': 'ꜱ', 't': 'ᴛ',
        'u': 'ᴜ', 'v': 'ᴠ', 'w': 'ᴡ', 'x': 'x', 'y': 'ʏ', 'z': 'ᴢ'
    },
    # Superscript style
    'superscript': {
        'A': 'ᴬ', 'B': 'ᴮ', 'C': 'ᶜ', 'D': 'ᴰ', 'E': 'ᴱ', 'F': 'ᶠ', 'G': 'ᴳ', 'H': 'ᴴ', 'I': 'ᴵ', 'J': 'ᴶ',
        'K': 'ᴷ', 'L': 'ᴸ', 'M': 'ᴹ', 'N': 'ᴺ', 'O': 'ᴼ', 'P': 'ᴾ', 'Q': 'Q', 'R': 'ᴿ', 'S': 'ˢ', 'T': 'ᵀ',
        'U': 'ᵁ', 'V': 'ⱽ', 'W': 'ᵂ', 'X': 'ˣ', 'Y': 'ʸ', 'Z': 'ᶻ',
        'a': 'ᵃ', 'b': 'ᵇ', 'c': 'ᶜ', 'd': 'ᵈ', 'e': 'ᵉ', 'f': 'ᶠ', 'g': 'ᵍ', 'h': 'ʰ', 'i': 'ⁱ', 'j': 'ʲ',
        'k': 'ᵏ', 'l': 'ˡ', 'm': 'ᵐ', 'n': 'ⁿ', 'o': 'ᵒ', 'p': 'ᵖ', 'q': 'q', 'r': 'ʳ', 's': 'ˢ', 't': 'ᵗ',
        'u': 'ᵘ', 'v': 'ᵛ', 'w': 'ʷ', 'x': 'ˣ', 'y': 'ʸ', 'z': 'ᶻ',
        '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹',
        '+': '⁺', '-': '⁻', '=': '⁼', '(': '⁽', ')': '⁾'
    },
    # Subscript style
    'subscript': {
        'A': 'ₐ', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'ₑ', 'F': 'F', 'G': 'G', 'H': 'ₕ', 'I': 'ᵢ', 'J': 'ⱼ',
        'K': 'ₖ', 'L': 'ₗ', 'M': 'ₘ', 'N': 'ₙ', 'O': 'ₒ', 'P': 'ₚ', 'Q': 'Q', 'R': 'ᵣ', 'S': 'ₛ', 'T': 'ₜ',
        'U': 'ᵤ', 'V': 'ᵥ', 'W': 'W', 'X': 'ₓ', 'Y': 'Y', 'Z': 'Z',
        'a': 'ₐ', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'ₑ', 'f': 'f', 'g': 'g', 'h': 'ₕ', 'i': 'ᵢ', 'j': 'ⱼ',
        'k': 'ₖ', 'l': 'ₗ', 'm': 'ₘ', 'n': 'ₙ', 'o': 'ₒ', 'p': 'ₚ', 'q': 'q', 'r': 'ᵣ', 's': 'ₛ', 't': 'ₜ',
        'u': 'ᵤ', 'v': 'ᵥ', 'w': 'w', 'x': 'ₓ', 'y': 'y', 'z': 'z',
        '0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄', '5': '₅', '6': '₆', '7': '₇', '8': '₈', '9': '₉',
        '+': '₊', '-': '₋', '=': '₌', '(': '₍', ')': '₎'
    },
    # Bubble text (circled)
    'bubble_text': {
        'A': 'Ⓐ', 'B': 'Ⓑ', 'C': 'Ⓒ', 'D': 'Ⓓ', 'E': 'Ⓔ', 'F': 'Ⓕ', 'G': 'Ⓖ', 'H': 'Ⓗ', 'I': 'Ⓘ', 'J': 'Ⓙ',
        'K': 'Ⓚ', 'L': 'Ⓛ', 'M': 'Ⓜ', 'N': 'Ⓝ', 'O': 'Ⓞ', 'P': 'Ⓟ', 'Q': 'Ⓠ', 'R': 'Ⓡ', 'S': 'Ⓢ', 'T': 'Ⓣ',
        'U': 'Ⓤ', 'V': 'Ⓥ', 'W': 'Ⓦ', 'X': 'Ⓧ', 'Y': 'Ⓨ', 'Z': 'Ⓩ',
        'a': 'ⓐ', 'b': 'ⓑ', 'c': 'ⓒ', 'd': 'ⓓ', 'e': 'ⓔ', 'f': 'ⓕ', 'g': 'ⓖ', 'h': 'ⓗ', 'i': 'ⓘ', 'j': 'ⓙ',
        'k': 'ⓚ', 'l': 'ⓛ', 'm': 'ⓜ', 'n': 'ⓝ', 'o': 'ⓞ', 'p': 'ⓟ', 'q': 'ⓠ', 'r': 'ⓡ', 's': 'ⓢ', 't': 'ⓣ',
        'u': 'ⓤ', 'v': 'ⓥ', 'w': 'ⓦ', 'x': 'ⓧ', 'y': 'ⓨ', 'z': 'ⓩ',
        '0': '⓪', '1': '①', '2': '②', '3': '③', '4': '④', '5': '⑤', '6': '⑥', '7': '⑦', '8': '⑧', '9': '⑨'
    },
    # Black bubble text (negative circled)
    'black_bubble_text': {
        'A': '🅐', 'B': '🅑', 'C': '🅒', 'D': '🅓', 'E': '🅔', 'F': '🅕', 'G': '🅖', 'H': '🅗', 'I': '🅘', 'J': '🅙',
        'K': '🅚', 'L': '🅛', 'M': '🅜', 'N': '🅝', 'O': '🅞', 'P': '🅟', 'Q': '🅠', 'R': '🅡', 'S': '🅢', 'T': '🅣',
        'U': '🅤', 'V': '🅥', 'W': '🅦', 'X': '🅧', 'Y': '🅨', 'Z': '🅩',
        'a': '🅐', 'b': '🅑', 'c': '🅒', 'd': '🅓', 'e': '🅔', 'f': '🅕', 'g': '🅖', 'h': '🅗', 'i': '🅘', 'j': '🅙',
        'k': '🅚', 'l': '🅛', 'm': '🅜', 'n': '🅝', 'o': '🅞', 'p': '🅟', 'q': '🅠', 'r': '🅡', 's': '🅢', 't': '🅣',
        'u': '🅤', 'v': '🅥', 'w': '🅦', 'x': '🅧', 'y': '🅨', 'z': '🅩',
        '0': '⓿', '1': '❶', '2': '❷', '3': '❸', '4': '❹', '5': '❺', '6': '❻', '7': '❼', '8': '❽', '9': '❾'
    },
    # Square text
    'square_text': {
        'A': '🄰', 'B': '🄱', 'C': '🄲', 'D': '🄳', 'E': '🄴', 'F': '🄵', 'G': '🄶', 'H': '🄷', 'I': '🄸', 'J': '🄹',
        'K': '🄺', 'L': '🄻', 'M': '🄼', 'N': '🄽', 'O': '🄾', 'P': '🄿', 'Q': '🅀', 'R': '🅁', 'S': '🅂', 'T': '🅃',
        'U': '🅄', 'V': '🅅', 'W': '🅆', 'X': '🅇', 'Y': '🅈', 'Z': '🅉',
        'a': '🄰', 'b': '🄱', 'c': '🄲', 'd': '🄳', 'e': '🄴', 'f': '🄵', 'g': '🄶', 'h': '🄷', 'i': '🄸', 'j': '🄹',
        'k': '🄺', 'l': '🄻', 'm': '🄼', 'n': '🄽', 'o': '🄾', 'p': '🄿', 'q': '🅀', 'r': '🅁', 's': '🅂', 't': '🅃',
        'u': '🅄', 'v': '🅅', 'w': '🅆', 'x': '🅇', 'y': '🅈', 'z': '🅉'
    },
    # Upside down text
    'upside_down': {
        'A': '∀', 'B': 'ᗺ', 'C': 'Ɔ', 'D': 'ᗡ', 'E': 'Ǝ', 'F': 'ᖴ', 'G': 'פ', 'H': 'H', 'I': 'I', 'J': 'ſ',
        'K': 'ʞ', 'L': '˥', 'M': 'W', 'N': 'N', 'O': 'O', 'P': 'Ԁ', 'Q': 'Q', 'R': 'ᴿ', 'S': 'S', 'T': '┴',
        'U': '∩', 'V': 'Λ', 'W': 'M', 'X': 'X', 'Y': '⅄', 'Z': 'Z',
        'a': 'ɐ', 'b': 'q', 'c': 'ɔ', 'd': 'p', 'e': 'ǝ', 'f': 'ɟ', 'g': 'ƃ', 'h': 'ɥ', 'i': 'ᴉ', 'j': 'ɾ',
        'k': 'ʞ', 'l': 'l', 'm': 'ɯ', 'n': 'u', 'o': 'o', 'p': 'd', 'q': 'b', 'r': 'ɹ', 's': 's', 't': 'ʇ',
        'u': 'n', 'v': 'ʌ', 'w': 'ʍ', 'x': 'x', 'y': 'ʎ', 'z': 'z',
        '0': '0', '1': 'Ɩ', '2': 'ᄅ', '3': 'Ɛ', '4': 'ㄣ', '5': 'ϛ', '6': '9', '7': 'ㄥ', '8': '8', '9': '6',
        '.': '˙', ',': "'", '?': '¿', '!': '¡', "'": ',', '"': '„', '(': ')', ')': '('
    },
    # Parenthesized text
    'parenthesized': {
        'A': '⒜', 'B': '⒝', 'C': '⒞', 'D': '⒟', 'E': '⒠', 'F': '⒡', 'G': '⒢', 'H': '⒣', 'I': '⒤', 'J': '⒥',
        'K': '⒦', 'L': '⒧', 'M': '⒨', 'N': '⒩', 'O': '⒪', 'P': '⒫', 'Q': '⒬', 'R': '⒭', 'S': '⒮', 'T': '⒯',
        'U': '⒰', 'V': '⒱', 'W': '⒲', 'X': '⒳', 'Y': '⒴', 'Z': '⒵',
        'a': '⒜', 'b': '⒝', 'c': '⒞', 'd': '⒟', 'e': '⒠', 'f': '⒡', 'g': '⒢', 'h': '⒣', 'i': '⒤', 'j': '⒥',
        'k': '⒦', 'l': '⒧', 'm': '⒨', 'n': '⒩', 'o': '⒪', 'p': '⒫', 'q': '⒬', 'r': '⒭', 's': '⒮', 't': '⒯',
        'u': '⒰', 'v': '⒱', 'w': '⒲', 'x': '⒳', 'y': '⒴', 'z': '⒵',
        '1': '⑴', '2': '⑵', '3': '⑶', '4': '⑷', '5': '⑸', '6': '⑹', '7': '⑺', '8': '⑻', '9': '⑼', '0': '⑽'
    },
    # Regional indicator (flag-style)
    'regional_indicator': {
        'A': '🇦', 'B': '🇧', 'C': '🇨', 'D': '🇩', 'E': '🇪', 'F': '🇫', 'G': '🇬', 'H': '🇭', 'I': '🇮', 'J': '🇯',
        'K': '🇰', 'L': '🇱', 'M': '🇲', 'N': '🇳', 'O': '🇴', 'P': '🇵', 'Q': '🇶', 'R': '🇷', 'S': '🇸', 'T': '🇹',
        'U': '🇺', 'V': '🇻', 'W': '🇼', 'X': '🇽', 'Y': '🇾', 'Z': '🇿',
        'a': '🇦', 'b': '🇧', 'c': '🇨', 'd': '🇩', 'e': '🇪', 'f': '🇫', 'g': '🇬', 'h': '🇭', 'i': '🇮', 'j': '🇯',
        'k': '🇰', 'l': '🇱', 'm': '🇲', 'n': '🇳', 'o': '🇴', 'p': '🇵', 'q': '🇶', 'r': '🇷', 's': '🇸', 't': '🇹',
        'u': '🇺', 'v': '🇻', 'w': '🇼', 'x': '🇽', 'y': '🇾', 'z': '🇿'
    },
    # Weird/Zalgo-style text (using special Unicode characters)
    'weird_text': {
        'A': 'Ⱥ', 'B': 'Ƀ', 'C': 'Ȼ', 'D': 'Đ', 'E': 'Ɇ', 'F': 'Ƒ', 'G': 'Ǥ', 'H': 'Ħ', 'I': 'Ɨ', 'J': 'Ɉ',
        'K': 'Ꝁ', 'L': 'Ł', 'M': 'Ɱ', 'N': 'Ň', 'O': 'Ø', 'P': 'Ᵽ', 'Q': 'Ꝗ', 'R': 'Ɍ', 'S': 'Ş', 'T': 'Ŧ',
        'U': 'Ʉ', 'V': 'Ṽ', 'W': 'Ⱳ', 'X': 'Ӿ', 'Y': 'Ɏ', 'Z': 'Ƶ',
        'a': 'ⱥ', 'b': 'ƀ', 'c': 'ȼ', 'd': 'đ', 'e': 'ɇ', 'f': 'ƒ', 'g': 'ǥ', 'h': 'ħ', 'i': 'ɨ', 'j': 'ɉ',
        'k': 'ꝁ', 'l': 'ł', 'm': 'ɱ', 'n': 'ň', 'o': 'ø', 'p': 'ᵽ', 'q': 'ꝗ', 'r': 'ɍ', 's': 'ş', 't': 'ŧ',
        'u': 'ʉ', 'v': 'ṽ', 'w': 'ⱳ', 'x': 'ӿ', 'y': 'ɏ', 'z': 'ƶ'
    },
    # Cherokee-like text
    'cherokee_like': {
        'A': 'Ꭿ', 'B': 'Ᏸ', 'C': 'Ꮯ', 'D': 'Ꮷ', 'E': 'Ꭼ', 'F': 'Ꮀ', 'G': 'Ꮐ', 'H': 'Ꮋ', 'I': 'Ꭵ', 'J': 'Ꮰ',
        'K': 'Ꮶ', 'L': 'Ꮮ', 'M': 'Ꮇ', 'N': 'Ꮑ', 'O': 'Ꮎ', 'P': 'Ꮲ', 'Q': 'Ꮖ', 'R': 'Ꮢ', 'S': 'Ꮪ', 'T': 'Ꮏ',
        'U': 'Ꮜ', 'V': 'Ꮙ', 'W': 'Ꮿ', 'X': 'Ꮝ', 'Y': 'Ꮍ', 'Z': 'Ꮓ',
        'a': 'ꭿ', 'b': 'ᏸ', 'c': 'ꮯ', 'd': 'ꮷ', 'e': 'ꭼ', 'f': 'ꮀ', 'g': 'ꮐ', 'h': 'ꮋ', 'i': 'ꭵ', 'j': 'ꮰ',
        'k': 'ꮶ', 'l': 'ꮮ', 'm': 'ꮇ', 'n': 'ꮑ', 'o': 'ꮎ', 'p': 'ꮲ', 'q': 'ꮖ', 'r': 'ꮢ', 's': 'ꮪ', 't': 'ꮏ',
        'u': 'ꮜ', 'v': 'ꮙ', 'w': 'ꮿ', 'x': 'ꮝ', 'y': 'ꮍ', 'z': 'ꮓ'
    },
    # Math-style variations
    'math_bold_digits': {
        '0': '𝟎', '1': '𝟏', '2': '𝟐', '3': '𝟑', '4': '𝟒', '5': '𝟓', '6': '𝟔', '7': '𝟕', '8': '𝟖', '9': '𝟗'
    },
    'math_double_struck_digits': {
        '0': '𝟘', '1': '𝟙', '2': '𝟚', '3': '𝟛', '4': '𝟜', '5': '𝟝', '6': '𝟞', '7': '𝟟', '8': '𝟠', '9': '𝟡'
    },
    'math_sans_serif_digits': {
        '0': '𝟢', '1': '𝟣', '2': '𝟤', '3': '𝟥', '4': '𝟦', '5': '𝟧', '6': '𝟨', '7': '𝟩', '8': '𝟪', '9': '𝟫'
    },
    'math_sans_bold_digits': {
        '0': '𝟬', '1': '𝟭', '2': '𝟮', '3': '𝟯', '4': '𝟰', '5': '𝟱', '6': '𝟲', '7': '𝟳', '8': '𝟴', '9': '𝟵'
    },
    'math_monospace_digits': {
        '0': '𝟶', '1': '𝟷', '2': '𝟸', '3': '𝟹', '4': '𝟺', '5': '𝟻', '6': '𝟼', '7': '𝟽', '8': '𝟾', '9': '𝟿'
    }
}

# Combining marks for diacritics
COMBINING_MARKS = {
    'underline': '\u0332',
    'strikethrough': '\u0336',
    'double_underline': '\u0333',
    'overline': '\u0305',
    'double_overline': '\u033F',
    'circle': '\u20DD',
    'slash': '\u0338',
    # Additional combining marks
    'tilde': '\u0303',
    'macron': '\u0304',
    'breve': '\u0306',
    'dot_above': '\u0307',
    'diaeresis': '\u0308',
    'hook_above': '\u0309',
    'ring_above': '\u030A',
    'double_acute': '\u030B',
    'caron': '\u030C',
    'vertical_line_above': '\u030D',
    'double_vertical_line_above': '\u030E',
    'double_grave': '\u030F',
    'candrabindu': '\u0310',
    'inverted_breve': '\u0311',
    'turned_comma_above': '\u0312',
    'comma_above': '\u0313',
    'reversed_comma_above': '\u0314',
    'comma_above_right': '\u0315',
    'grave_below': '\u0316',
    'acute_below': '\u0317',
    'left_tack_below': '\u0318',
    'right_tack_below': '\u0319',
    'left_angle_above': '\u031A',
    'horn': '\u031B',
    'left_half_ring_below': '\u031C',
    'up_tack_below': '\u031D',
    'down_tack_below': '\u031E',
    'plus_below': '\u031F',
    'minus_below': '\u0320',
    'palatalized_hook_below': '\u0321',
    'retroflex_hook_below': '\u0322',
    'dot_below': '\u0323',
    'diaeresis_below': '\u0324',
    'ring_below': '\u0325',
    'comma_below': '\u0326',
    'cedilla': '\u0327',
    'ogonek': '\u0328',
    'vertical_line_below': '\u0329',
    'bridge_below': '\u032A',
    'inverted_double_arch_below': '\u032B',
    'caron_below': '\u032C',
    'circumflex_below': '\u032D',
    'breve_below': '\u032E',
    'inverted_breve_below': '\u032F',
    'tilde_below': '\u0330',
    'macron_below': '\u0331',
    'low_line': '\u0332',
    'double_low_line': '\u0333',
    'tilde_overlay': '\u0334',
    'short_stroke_overlay': '\u0335',
    'long_stroke_overlay': '\u0336',
    'short_solidus_overlay': '\u0337',
    'long_solidus_overlay': '\u0338',
    'right_half_ring_below': '\u0339',
    'inverted_bridge_below': '\u033A',
    'square_below': '\u033B',
    'seagull_below': '\u033C',
    'x_above': '\u033D',
    'vertical_tilde': '\u033E',
    'double_overline': '\u033F',
    'grave_tone_mark': '\u0340',
    'acute_tone_mark': '\u0341',
    'greek_perispomeni': '\u0342',
    'greek_koronis': '\u0343',
    'greek_dialytika_tonos': '\u0344',
    'greek_ypogegrammeni': '\u0345',
    'bridge_above': '\u0346',
    'equals_below': '\u0347',
    'double_vertical_line_below': '\u0348',
    'left_angle_below': '\u0349',
    'not_tilde_above': '\u034A',
    'homothetic_above': '\u034B',
    'almost_equal_above': '\u034C',
    'left_right_arrow_below': '\u034D',
    'upwards_arrow_below': '\u034E',
    'grapheme_joiner': '\u034F'
}

# Vietnamese language support
VIETNAMESE_CHARACTERS = {
    # Basic Vietnamese alphabet with diacritics
    'A': 'A', 'Ă': 'Ă', 'Â': 'Â', 'B': 'B', 'C': 'C', 'D': 'D', 'Đ': 'Đ', 'E': 'E', 'Ê': 'Ê',
    'G': 'G', 'H': 'H', 'I': 'I', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O', 'Ô': 'Ô', 'Ơ': 'Ơ',
    'P': 'P', 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T', 'U': 'U', 'Ư': 'Ư', 'V': 'V', 'X': 'X', 'Y': 'Y',
    'a': 'a', 'ă': 'ă', 'â': 'â', 'b': 'b', 'c': 'c', 'd': 'd', 'đ': 'đ', 'e': 'e', 'ê': 'ê',
    'g': 'g', 'h': 'h', 'i': 'i', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'ô': 'ô', 'ơ': 'ơ',
    'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'u': 'u', 'ư': 'ư', 'v': 'v', 'x': 'x', 'y': 'y',

    # Vietnamese characters with tone marks
    # A family
    'À': 'À', 'Á': 'Á', 'Ả': 'Ả', 'Ã': 'Ã', 'Ạ': 'Ạ',
    'à': 'à', 'á': 'á', 'ả': 'ả', 'ã': 'ã', 'ạ': 'ạ',

    # Ă family
    'Ằ': 'Ằ', 'Ắ': 'Ắ', 'Ẳ': 'Ẳ', 'Ẵ': 'Ẵ', 'Ặ': 'Ặ',
    'ằ': 'ằ', 'ắ': 'ắ', 'ẳ': 'ẳ', 'ẵ': 'ẵ', 'ặ': 'ặ',

    # Â family
    'Ầ': 'Ầ', 'Ấ': 'Ấ', 'Ẩ': 'Ẩ', 'Ẫ': 'Ẫ', 'Ậ': 'Ậ',
    'ầ': 'ầ', 'ấ': 'ấ', 'ẩ': 'ẩ', 'ẫ': 'ẫ', 'ậ': 'ậ',

    # E family
    'È': 'È', 'É': 'É', 'Ẻ': 'Ẻ', 'Ẽ': 'Ẽ', 'Ẹ': 'Ẹ',
    'è': 'è', 'é': 'é', 'ẻ': 'ẻ', 'ẽ': 'ẽ', 'ẹ': 'ẹ',

    # Ê family
    'Ề': 'Ề', 'Ế': 'Ế', 'Ể': 'Ể', 'Ễ': 'Ễ', 'Ệ': 'Ệ',
    'ề': 'ề', 'ế': 'ế', 'ể': 'ể', 'ễ': 'ễ', 'ệ': 'ệ',

    # I family
    'Ì': 'Ì', 'Í': 'Í', 'Ỉ': 'Ỉ', 'Ĩ': 'Ĩ', 'Ị': 'Ị',
    'ì': 'ì', 'í': 'í', 'ỉ': 'ỉ', 'ĩ': 'ĩ', 'ị': 'ị',

    # O family
    'Ò': 'Ò', 'Ó': 'Ó', 'Ỏ': 'Ỏ', 'Õ': 'Õ', 'Ọ': 'Ọ',
    'ò': 'ò', 'ó': 'ó', 'ỏ': 'ỏ', 'õ': 'õ', 'ọ': 'ọ',

    # Ô family
    'Ồ': 'Ồ', 'Ố': 'Ố', 'Ổ': 'Ổ', 'Ỗ': 'Ỗ', 'Ộ': 'Ộ',
    'ồ': 'ồ', 'ố': 'ố', 'ổ': 'ổ', 'ỗ': 'ỗ', 'ộ': 'ộ',

    # Ơ family
    'Ờ': 'Ờ', 'Ớ': 'Ớ', 'Ở': 'Ở', 'Ỡ': 'Ỡ', 'Ợ': 'Ợ',
    'ờ': 'ờ', 'ớ': 'ớ', 'ở': 'ở', 'ỡ': 'ỡ', 'ợ': 'ợ',

    # U family
    'Ù': 'Ù', 'Ú': 'Ú', 'Ủ': 'Ủ', 'Ũ': 'Ũ', 'Ụ': 'Ụ',
    'ù': 'ù', 'ú': 'ú', 'ủ': 'ủ', 'ũ': 'ũ', 'ụ': 'ụ',

    # Ư family
    'Ừ': 'Ừ', 'Ứ': 'Ứ', 'Ử': 'Ử', 'Ữ': 'Ữ', 'Ự': 'Ự',
    'ừ': 'ừ', 'ứ': 'ứ', 'ử': 'ử', 'ữ': 'ữ', 'ự': 'ự',

    # Y family
    'Ỳ': 'Ỳ', 'Ý': 'Ý', 'Ỷ': 'Ỷ', 'Ỹ': 'Ỹ', 'Ỵ': 'Ỵ',
    'ỳ': 'ỳ', 'ý': 'ý', 'ỷ': 'ỷ', 'ỹ': 'ỹ', 'ỵ': 'ỵ'
}

# Vietnamese tone marks
VIETNAMESE_TONE_MARKS = {
    'grave': '\u0300',      # à
    'acute': '\u0301',      # á
    'hook_above': '\u0309', # ả
    'tilde': '\u0303',      # ã
    'dot_below': '\u0323'   # ạ
}

def is_vietnamese_text(text):
    """
    Detect if text contains Vietnamese characters
    """
    vietnamese_chars = set(VIETNAMESE_CHARACTERS.keys())
    text_chars = set(text)

    # Check if any Vietnamese-specific characters are present
    vietnamese_specific = {
        'ă', 'â', 'đ', 'ê', 'ô', 'ơ', 'ư',
        'Ă', 'Â', 'Đ', 'Ê', 'Ô', 'Ơ', 'Ư'
    }

    # Also check for Vietnamese tone marks
    vietnamese_toned = {
        'à', 'á', 'ả', 'ã', 'ạ', 'ằ', 'ắ', 'ẳ', 'ẵ', 'ặ', 'ầ', 'ấ', 'ẩ', 'ẫ', 'ậ',
        'è', 'é', 'ẻ', 'ẽ', 'ẹ', 'ề', 'ế', 'ể', 'ễ', 'ệ', 'ì', 'í', 'ỉ', 'ĩ', 'ị',
        'ò', 'ó', 'ỏ', 'õ', 'ọ', 'ồ', 'ố', 'ổ', 'ỗ', 'ộ', 'ờ', 'ớ', 'ở', 'ỡ', 'ợ',
        'ù', 'ú', 'ủ', 'ũ', 'ụ', 'ừ', 'ứ', 'ử', 'ữ', 'ự', 'ỳ', 'ý', 'ỷ', 'ỹ', 'ỵ',
        'À', 'Á', 'Ả', 'Ã', 'Ạ', 'Ằ', 'Ắ', 'Ẳ', 'Ẵ', 'Ặ', 'Ầ', 'Ấ', 'Ẩ', 'Ẫ', 'Ậ',
        'È', 'É', 'Ẻ', 'Ẽ', 'Ẹ', 'Ề', 'Ế', 'Ể', 'Ễ', 'Ệ', 'Ì', 'Í', 'Ỉ', 'Ĩ', 'Ị',
        'Ò', 'Ó', 'Ỏ', 'Õ', 'Ọ', 'Ồ', 'Ố', 'Ổ', 'Ỗ', 'Ộ', 'Ờ', 'Ớ', 'Ở', 'Ỡ', 'Ợ',
        'Ù', 'Ú', 'Ủ', 'Ũ', 'Ụ', 'Ừ', 'Ứ', 'Ử', 'Ữ', 'Ự', 'Ỳ', 'Ý', 'Ỷ', 'Ỹ', 'Ỵ'
    }

    return bool(text_chars.intersection(vietnamese_specific.union(vietnamese_toned)))

def normalize_vietnamese_text(text):
    """
    Normalize Vietnamese text for processing
    """
    import unicodedata

    # Normalize to NFD (decomposed form) to separate base characters from diacritics
    normalized = unicodedata.normalize('NFD', text)
    return normalized

def style_vietnamese_text(text, style_name):
    """
    Apply text styling to Vietnamese text while preserving tone marks and diacritics
    """
    import unicodedata

    if style_name not in STYLE_CONFIG:
        return text

    style_map = STYLE_CONFIG[style_name]
    result = []

    # Normalize text to handle composed characters
    normalized_text = normalize_vietnamese_text(text)

    i = 0
    while i < len(normalized_text):
        char = normalized_text[i]

        # Check if this is a base character that can be styled
        if char in style_map:
            styled_char = style_map[char]
            result.append(styled_char)

            # Look ahead for combining marks (tone marks, diacritics)
            j = i + 1
            while j < len(normalized_text) and unicodedata.category(normalized_text[j]).startswith('M'):
                result.append(normalized_text[j])  # Preserve combining marks
                j += 1
            i = j
        else:
            # Character not in style map, keep as is
            result.append(char)
            i += 1

    # Normalize back to NFC (composed form) for display
    return unicodedata.normalize('NFC', ''.join(result))

def get_vietnamese_language_info():
    """
    Get information about Vietnamese language support
    """
    return {
        'language': 'Vietnamese',
        'language_code': 'vi',
        'script': 'Latin with Vietnamese extensions',
        'characters_supported': len(VIETNAMESE_CHARACTERS),
        'tone_marks': list(VIETNAMESE_TONE_MARKS.keys()),
        'special_characters': ['ă', 'â', 'đ', 'ê', 'ô', 'ơ', 'ư'],
        'description': 'Vietnamese language support with proper handling of diacritics and tone marks'
    }

# ========================
# CORE FUNCTIONS
# ========================
def style_text(text, style):
    """
    Convert regular text to styled unicode text.
    
    Args:
        text (str): Input text to style
        style (str): Style to apply (must be a key in STYLE_CONFIG)
        
    Returns:
        str: Text with the specified style applied
    """
    if style not in STYLE_CONFIG:
        return text
        
    result = ""
    for char in text:
        if char in STYLE_CONFIG[style]:
            result += STYLE_CONFIG[style][char]
        else:
            result += char
    return result

def add_diacritics(text, marks):
    """
    Add specified combining diacritical marks to each character in text.
    
    Args:
        text (str): Input text
        marks (list): List of combining marks to add
        
    Returns:
        str: Text with diacritical marks added
    """
    result = ""
    for char in text:
        marked_char = char
        for mark in marks:
            marked_char += mark
        result += marked_char
    return result

# ========================
# DEMONSTRATION & OUTPUT
# ========================
def generate_demo(input_text: str) -> str:
    output = []
    
    # Generate styled text samples
    for style in STYLE_CONFIG.keys():
        styled = style_text(input_text, style)
        output.append(f"## {style.replace('_', ' ').title()}")
        output.append(styled + '\n')
    
    # Generate combined diacritics
    output.append("## Combined Diacritical Marks")
    for mark_count in range(1, len(COMBINING_MARKS)+1):
        marks = list(COMBINING_MARKS.values())[:mark_count]
        styled = style_text(input_text, 'bold')
        marked = add_diacritics(styled, marks)
        output.append(f"### {mark_count} Marks: {' + '.join(unicodedata.name(m) for m in marks)}")
        output.append(marked + '\n')
    
    return '\n'.join(output)

# ========================
# EXECUTION
# ========================
if __name__ == "__main__":
    input_str = "The quick brown fox jumps over the lazy dog. 0123456789"  # Test with mixed case and digits
    
    demo_content = generate_demo(input_str)
    
    with open('unicode_styles_corrected.txt', 'w', encoding='utf-8') as f:
        f.write(demo_content)
    
    print("Successfully generated unicode_styles_corrected.txt")

