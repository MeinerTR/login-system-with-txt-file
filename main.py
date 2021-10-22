from re import findall
from random import seed
from os import path as path
from getpass import getpass
from os import system as sys
from random import randrange

class Seed:
    def __init__(self):
        self.seed = 0
        self.number = len(all_things)

    def get_seed(self, seed_='42'):
        if seed_ == '42':
            self.seed = randrange(self.number)
            seed(self.seed)
        if not seed_ == '42':
            self.seed = seed_
            seed(self.seed)

    def get_values(self, seed_=42, pos=3, lst=[]):
        values = []
        self.get_seed(seed_)
        for wait in range(pos):
            nthng = randrange(self.number)
        for brb in range(5):
            if len(lst) < 1:
                values.append(randrange(self.number))
            if len(lst) > 1:
                pos = randrange(self.number)
                values.append(lst[pos])
        return values

all_things = [
    thing for thing in "a æ b ɓ ƃ c ƈ d đ ɖ ɗ ƌ ð e ǝ ə ɛ f ƒ g ǥ ɠ ɣ ƣ h ƕ ħ i ı ɨ ɩ j k ƙ l ł ƚ m n ɲ ƞ ŋ o œ ø ɔ ɵ ȣ p ƥ q r ʀ s ʃ t ŧ ƭ ʈ u ɯ ʊ v ʋ w x y ƴ z ƶ ȥ ʒ ƹ ȝ þ ƿ ƨ ƽ ƅ ʔ ɐ ɑ ɒ ʙ ƀ ɕ ʣ ʥ ʤ ɘ ɚ ɜ ɝ ɞ ʚ ɤ ʩ ɡ ɢ ʛ ʜ ɦ ɧ ɪ ʝ ɟ ʄ ʞ ʪ ʫ ʟ ɫ ɬ ɭ ɮ ƛ ʎ ɱ ɴ ɳ ɶ ɷ ɸ ʠ ĸ ɹ ɺ ɻ ɼ ɽ ɾ ɿ ʁ ʂ ƪ ʅ ʆ ʨ ƾ ʦ ʧ ƫ ʇ ʉ ɥ ɰ ʌ ʍ ʏ ƍ ʐ ʑ ƺ ʓ ƻ ʕ ʡ ʢ ʖ ǀ ǁ ǂ ǃ ʗ ʘ ʬ ʭá à ă ắ ằ ẵ ẳ â ấ ầ ẫ ẩ ǎ å ǻ ä ǟ ã ȧ ǡ ą ā ả ȁ ȃ ạ ặ ậ ḁ ǽ ǣ ḃ ḅ ḇ ć ĉ č ċ ç ḉ ď ḋ ḑ ḍ ḓ ḏ é è ĕ ê ế ề ễ ể ě ë ẽ ė ȩ ḝ ę ē ḗ ḕ ẻ ȅ ȇ ẹ ệ ḙ ḛ ḟ ǵ ğ ĝ ǧ ġ ģ ḡ ĥ ȟ ḧ ḣ ḩ ḥ ḫ ẖ í ì ĭ î ǐ ï ḯ ĩ į ī ỉ ȉ ȋ ị ḭ ĵ ǰ ḱ ǩ ķ ḳ ḵ ĺ ľ ļ ḷ ḹ ḽ ḻ ḿ ṁ ṃ ń ǹ ň ñ ṅ ņ ṇ ṋ ṉ ó ò ŏ ô ố ồ ỗ ổ ǒ ö ȫ ő õ ṍ ṏ ȭ ȯ ȱ ǫ ǭ ō ṓ ṑ ỏ ȍ ȏ ơ ớ ờ ỡ ở ợ ọ ộ ǿ ṕ ṗ ŕ ř ṙ ŗ ȑ ȓ ṛ ṝ ṟ ś ṥ ŝ š ṧ ṡ ş ṣ ṩ ș ť ẗ ṫ ţ ṭ ț ṱ ṯ ú ù ŭ û ǔ ů ü ǘ ǜ ǚ ǖ ű ũ ṹ ų ū ṻ ủ ȕ ȗ ư ứ ừ ữ ử ự ụ ṳ ṷ ṵ ṽ ṿ ẃ ẁ ŵ ẘ ẅ ẇ ẉ ẍ ẋ ý ỳ ŷ ẙ ÿ ỹ ẏ ȳ ỷ ỵ ź ẑ ž ż ẓ ẕ ǯ A Æ B Ɓ Ƃ C Ƈ D Đ Ɖ Ɗ Ƌ Ð E Ǝ Ə Ɛ F Ƒ G Ǥ Ɠ Ɣ Ƣ H Ƕ Ħ I Ɨ Ɩ J K Ƙ L Ł M N Ɲ Ƞ Ŋ O Œ Ø Ɔ Ɵ Ȣ P Ƥ Q R Ʀ S ß Ʃ T Ŧ Ƭ Ʈ U Ɯ Ʊ V Ʋ W X Y Ƴ Z Ƶ Ȥ Ʒ Ƹ Ȝ Þ Ƿ Ƨ Ƽ Ƅ Á À Ă Ắ Ằ Ẵ Ẳ Â Ấ Ầ Ẫ Ẩ Ǎ Å Ǻ Ä Ǟ Ã Ȧ Ǡ Ą Ā Ả Ȁ Ȃ Ạ Ặ Ậ Ḁ Ǽ Ǣ Ḃ Ḅ Ḇ Ć Ĉ Č Ċ Ç Ḉ Ď Ḋ Ḑ Ḍ Ḓ Ḏ É È Ĕ Ê Ế Ề Ễ Ể Ě Ë Ẽ Ė Ȩ Ḝ Ę Ē Ḗ Ḕ Ẻ Ȅ Ȇ Ẹ Ệ Ḙ Ḛ Ḟ Ǵ Ğ Ĝ Ǧ Ġ Ģ Ḡ Ĥ Ȟ Ḧ Ḣ Ḩ Ḥ Ḫ Í Ì Ĭ Î Ǐ Ï Ḯ Ĩ İ Į Ī Ỉ Ȉ Ȋ Ị Ḭ Ĵ Ḱ Ǩ Ķ Ḳ Ḵ Ĺ Ľ Ļ Ḷ Ḹ Ḽ Ḻ Ḿ Ṁ Ṃ Ń Ǹ Ň Ñ Ṅ Ņ Ṇ Ṋ Ṉ Ó Ò Ŏ Ô Ố Ồ Ỗ Ổ Ǒ Ö Ȫ Ő Õ Ṍ Ṏ Ȭ Ȯ Ȱ Ǫ Ǭ Ō Ṓ Ṑ Ỏ Ȍ Ȏ Ơ Ớ Ờ Ỡ Ở Ợ Ọ Ộ Ǿ Ṕ Ṗ Ŕ Ř Ṙ Ŗ Ȑ Ȓ Ṛ Ṝ Ṟ Ś Ṥ Ŝ Š Ṧ Ṡ Ş Ṣ Ṩ Ș Ť Ṫ Ţ Ṭ Ț Ṱ Ṯ Ú Ù Ŭ Û Ǔ Ů Ü Ǘ Ǜ Ǚ Ǖ Ű Ũ Ṹ Ų Ū Ṻ Ủ Ȕ Ȗ Ư Ứ Ừ Ữ Ử Ự Ụ Ṳ Ṷ Ṵ Ṽ Ṿ Ẃ Ẁ Ŵ Ẅ Ẇ Ẉ Ẍ Ẋ Ý Ỳ Ŷ Ÿ Ỹ Ẏ Ȳ Ỷ Ỵ Ź Ẑ Ž Ż Ẓ Ẕ Ǯ ａ Ａ ª Å ẚ ｂ Ｂ ｃ Ｃ ｄ Ｄ ǳ ǲ Ǳ ǆ ǅ Ǆ ｅ Ｅ ｆ Ｆ ﬀ ﬃ ﬄ ﬁ ﬂ ｇ Ｇ ˠ ｈ Ｈ ʰ ʱ ｉ Ｉ ⁱ ĳ Ĳ ｊ Ｊ ʲ ｋ K Ｋ ｌ Ｌ ˡ ŀ Ŀ ǉ ǈ Ǉ ｍ Ｍ ｎ Ｎ ⁿ ǌ ǋ Ǌ ｏ Ｏ º ｐ Ｐ ｑ Ｑ ｒ Ｒ ʳ ʴ ʵ ʶ ｓ Ｓ ˢ ſ ẛ ﬆ ﬅ ｔ Ｔ ｕ Ｕ ｖ Ｖ ｗ Ｗ ʷ ｘ Ｘ ˣ ｙ Ｙ ʸ ｚ Ｚ ŉ ˤ ᴬ ᵃ ᴀ ᴭ ᴁ ᴂ ᵆ ᵄ ᵅ ᴮ ᵇ ᴯ ᴃ ᴄ ᴰ ᵈ ᴅ ȡ ᴆ ᴱ ᵉ ᴇ ᴲ ᵊ ᵋ ᴈ ᵌ ᴳ ᵍ ᴴ ᴵ ᵢ ᴉ ᵎ ᴶ ᴊ ᴷ ᵏ ᴋ ᴸ ᴌ ȴ ᴹ ᵐ ᴍ ᴺ ᴻ ᴎ ȵ ᵑ ᴼ ᵒ ᴏ ᴑ ᴔ ᴓ ᵓ ᴐ ᴒ ᴖ ᵔ ᴗ ᵕ ᴽ ᴕ ᴾ ᵖ ᴘ ᴿ ᵣ ᴙ ᴚ ᵀ ᵗ ᴛ ȶ ᵁ ᵘ ᵤ ᴜ ᴝ ᵙ ᴞ ᵫ ʮ ʯ ᵚ ᴟ ᵛ ᵥ ᴠ ᵂ ᴡ ᴢ ᴣ ᴤ ᴥ ᵜ ȷ ȸ ȹ Ⱥ Ȼ ȼ Ƚ Ⱦ ȿ ɀ Ɂ ᵬ ᵭ ᵮ ᵯ ᵰ ᵱ ᵲ ᵳ ᵴ ᵵ ᵶ ᵷ ᵹ ᵺ ᵻ ᵼ ᵽ ᵾ ᵿ ᶀ ᶁ ᶂ ᶃ ᶄ ᶅ ᶆ ᶇ ᶈ ᶉ ᶊ ᶋ ᶌ ᶍ ᶎ ᶏ ᶐ ᶑ ᶒ ᶓ ᶔ ᶕ ᶖ ᶗ ᶘ ᶙ ᶚ ᶛ ᶜ ᶝ ᶞ ᶟ ᶠ ᶡ ᶢ ᶣ ᶤ ᶥ ᶦ ᶧ ᶨ ᶩ ᶪ ᶫ ᶬ ᶭ ᶮ ᶯ ᶰ ᶱ ᶲ ᶳ ᶴ ᶵ ᶶ ᶷ ᶸ ᶹ ᶺ ᶻ ᶼ ᶽ ᶾ ᶿ ₐ ₑ ₒ ₓ ₔ α β γ δ ε ϝ ϛ ζ η θ ι κ λ μ ν ξ ο π ϟ ϙ ρ σ τ υ φ χ ψ ω ϡ ϳ ϗ ͵ ϶ ἀ ἄ ἂ ἆ ἁ ἅ ἃ ἇ ά ὰ ᾰ ᾶ ᾱ ἐ ἔ ἒ ἑ ἕ ἓ έ ὲ ἠ ἤ ἢ ἦ ἡ ἥ ἣ ἧ ή ὴ ῆ ἰ ἴ ἲ ἶ ἱ ἵ ἳ ἷ ί ὶ ῐ ῖ ϊ ΐ ῒ ῗ ῑ ὀ ὄ ὂ ὁ ὅ ὃ ό ὸ ῤ ῥ ὐ ὔ ὒ ὖ ὑ ὕ ὓ ὗ ύ ὺ ῠ ῦ ϋ ΰ ῢ ῧ ῡ ὠ ὤ ὢ ὦ ὡ ὥ ὣ ὧ ώ ὼ ῶ Α Β Γ Δ Ε Ϝ Ϛ Ζ Η Θ Ι Κ Λ Μ Ν Ξ Ο Π Ϟ Ϙ Ρ Σ ς Τ Υ Φ Χ Ψ Ω Ϡ Ἀ Ἄ ᾄ ᾌ Ἂ ᾂ ᾊ Ἆ ᾆ ᾎ ᾀ ᾈ Ἁ Ἅ ᾅ ᾍ Ἃ ᾃ ᾋ Ἇ ᾇ ᾏ ᾁ ᾉ Ά ᾴ Ὰ ᾲ Ᾰ ᾷ Ᾱ ᾳ ᾼ Ἐ Ἔ Ἒ Ἑ Ἕ Ἓ Έ Ὲ Ἠ Ἤ ᾔ ᾜ Ἢ ᾒ ᾚ Ἦ ᾖ ᾞ ᾐ ᾘ Ἡ Ἥ ᾕ ᾝ Ἣ ᾓ ᾛ Ἧ ᾗ ᾟ ᾑ ᾙ Ή ῄ Ὴ ῂ ῇ ῃ ῌ Ἰ Ἴ Ἲ Ἶ Ἱ Ἵ Ἳ Ἷ Ί Ὶ Ῐ Ϊ Ῑ Ὀ Ὄ Ὂ Ὁ Ὅ Ὃ Ό Ὸ Ῥ Ὑ Ὕ Ὓ Ὗ Ύ Ὺ Ῠ Ϋ Ῡ Ὠ Ὤ ᾤ ᾬ Ὢ ᾢ ᾪ Ὦ ᾦ ᾮ ᾠ ᾨ Ὡ Ὥ ᾥ ᾭ Ὣ ᾣ ᾫ Ὧ ᾧ ᾯ ᾡ ᾩ Ώ ῴ Ὼ ῲ ῷ ῳ ῼ ʹ ά Ά ϐ ϵ έ Έ ή Ή ϑ ϴ ι ί Ί ΐ ϰ ό Ό ϖ ϱ ϲ ϒ ύ Ύ ϓ ϔ ΰ ϕ Ω ώ Ώ ` ´ ΄ ΅ ΅ ῭ ῁ ᾽ ᾿ ῎ ῍ ῏ ῾ ῞ ῝ ῟ ῀ ᵝ ᵦ ᵞ ᵧ ᴦ ᵟ ͺ ᴧ ᴨ ᵨ ᴩ Ϲ ᵠ ᵩ ᵡ ᵪ ᴪ ϸ Ϸ ϻ Ϻ ϼ Ͻ Ͼ Ͽ а ә ӕ б в г ґ ғ ҕ д ԁ ђ ԃ ҙ е є ж җ з ԅ ѕ ӡ ԇ и ҋ і ј к қ ӄ ҡ ҟ ҝ л ӆ љ ԉ м ӎ н ӊ ң ӈ ҥ њ ԋ о ө п ҧ ҁ р ҏ с ԍ ҫ т ԏ ҭ ћ у ү ұ ѹ ф х ҳ һ ѡ ѿ ѽ ѻ ц ҵ ч ҷ ӌ ҹ ҽ ҿ џ ш щ ъ ы ь ҍ ѣ э ю я ѥ ѧ ѫ ѩ ѭ ѯ ѱ ѳ ѵ ҩ Ӏ ҃ ҄ ҅ ҆ ҈ ҉ ҂ ӑ ӓ ӛ ѓ ѐ ё ӗ ӂ ӝ ӟ ѝ ӣ ӥ ї й ӧ ӫ ќ ӯ ў ӱ ӳ ӵ ӹ ӭ ѷ А Ә Ӕ Б В Г Ґ Ғ Ҕ Д Ԁ Ђ Ԃ Ҙ Е Є Ж Җ З Ԅ Ѕ Ӡ Ԇ И Ҋ І Ј К Қ Ӄ Ҡ Ҟ Ҝ Л Ӆ Љ Ԉ М Ӎ Н Ӊ Ң Ӈ Ҥ Њ Ԋ О Ө П Ҧ Ҁ Р Ҏ С Ԍ Ҫ Т Ԏ Ҭ Ћ У Ү Ұ Ѹ Ф Х Ҳ Һ Ѡ Ѿ Ѽ Ѻ Ц Ҵ Ч Ҷ Ӌ Ҹ Ҽ Ҿ Џ Ш Щ Ъ Ы Ь Ҍ Ѣ Э Ю Я Ѥ Ѧ Ѫ Ѩ Ѭ Ѯ Ѱ Ѳ Ѵ Ҩ Ӑ Ӓ Ӛ Ѓ Ѐ Ё Ӗ Ӂ Ӝ Ӟ Ѝ Ӣ Ӥ Ї Й Ӧ Ӫ Ќ Ӯ Ў Ӱ Ӳ Ӵ Ӹ Ӭ Ѷ ᴫ Ӷ ӷ ᵸ ֊ ա բ գ դ ե զ է ը թ ժ ի լ խ ծ կ հ ձ ղ ճ մ յ ն շ ո չ պ ջ ռ ս վ տ ր ց ւ փ ք օ ֆ ՙ ՝ ՜ ՞ ՚ ՛ ՟ Ա Բ Գ Դ Ե Զ Է Ը Թ Ժ Ի Լ Խ Ծ Կ Հ Ձ Ղ Ճ Մ Յ Ն Շ Ո Չ Պ Ջ Ռ Ս Վ Տ Ր Ց Ւ Փ Ք Օ Ֆ և ﬔ ﬕ ﬗ ﬓ ﬖ  ۖ ۗ ۘ ۙ ۚ ۛ ۜ ۟ ۠ ۡ ۢ ۣ ۤ ۧ ۨ ۪ ۫ ۬ ۭ ﹳ ٴ ٲ ٱ ٳ ا ٮ  ړ ڔ ڕ ږ ڗ < > £ # - ½ { [ ] } \ | é ! ' ^ + % & / ( ) = ? _ ' @ € ₺ ~ æ ß´ ` > ` ".split()]

def get_pos(lst, char): # '==' is 'to'
    if char == ' ' or char == "'":
        return seed_.get_values(seed_.seed, randrange(len(all_things)))
    else:   return   [pos for pos, hello in enumerate(lst) if hello == char]

class main:
    def __init__(self):
        self.show = False

    def prepare(self):
        if not path.exists('data.txt'):
            with open('data.txt', 'w') as file:
                del self.prepare

    def start(self):
        self.prepare()
        while True:
            sys('cls')
            seed_.get_seed()
            print(' # menu #\n\n',

            '1 - login\n','2 - register\n')
            answer = str  (input('>>> '))
            if answer == str(1) or answer == str(2):
                break

        if answer == str(1): self.login()
        if answer == str(2): self.register()

    def login(self):
        with open('data.txt', 'r', encoding='utf-8') as file:
            input_ = file.readlines()

        def get_infr(input_):
            input_ = ''.join(input_)
            return input_.split('$')

        usern_, passw_ = get_infr(input_)

        _seed = ''.join(findall('\d+', passw_))
        _seed =        int                  (_seed)
        seed_.get_seed             (int(_seed))

        _usern = input('username: ')
        passw = getpass('password: ')
        _passw = self.get_filter(passw)
        _passw = self.get_seed_into(_passw, _seed)
        if _usern == usern_ and _passw == passw_:
            print('correct')
        else:
            print(1, _usern, 2, usern_)
            print(1, _passw, 2, passw_)

    def get_filter(self, passw):
        filtered_passw = []
        h         =         0
        for char in passw:
            h = 0 if h > 3 else h + 1
            pos = get_pos(all_things, char)[0]
            v = seed_.get_values(seed_.seed, int(pos), all_things)
            if h < 2:
                filtered_passw.append(v[h])
            if not h < 1:
                try: filtered_passw.append(v[h+1])
                except IndexError: filtered_passw.append(v[h])
        return ''.join(filtered_passw)

    def register(self):
        usern = input('username: ')
        passw = getpass('password: ')

        passw = self.get_filter(passw)

        passw = self.get_seed_into(passw, seed_.seed)

        with open('data.txt', 'w', encoding='utf-8') as file:
            file.write(f'{usern}${passw}')

    def get_seed_into(self, passw, seed):
        seed =                                     list(str(seed))
        seed.append                                           (' ')
        the_getded_passw = [char for char in passw]
        x                              =                              0
        for y in range(1, len(seed)+1):
            x = (int(len(passw) / len(seed)) * y)
            the_getded_passw.insert(x, seed[y-1])
        the_getded_passw = ''.join(the_getded_passw)
        return the_getded_passw.split                  (' ')[0]

main, seed_ = main(), Seed()
if __name__ == '__main__': main.start()
