from Enums_WinterIsComing import *

#---------------------------------------------
#DICTIONARIES
#----------------------------------------------
#text ID rules:
# xx     = Item
# xxx    = Spot/room
# xxxx   = combinations of item --> new item
# xxxxx  = combination of item and spot --> action
# xxxxxx = action within a room 


actionDict = {
    0 : " genauer untersuchen?\n",
    1 : " betreten?\n",
    2 : " öffnen?\n",
    3 : " benutzen?\n",
    4 : " nehmen?\n"
    }

#Text Dictionary by IDs:
dictTexts = {
    10 : \
"Euer Smartphone. Kann so ziemlich alles und ist natürlich auch mit Taschenlampe,\n\
Kamera und Navigationssystem ausgestattet.\n\
Hier draußen scheinen leider weder Mobilfunk noch Datenvervindung möglich zu sein.\n\
Zudem ist der Akkustand niedrig und Ihr habt keine Powerbank dabei.\n",
    11 : \
"Ein kaum leserliches Foto der Umgebungskare, aufgenommen mit dem Handy.\n\
Die Spiegelung der hellen Hauswand gegenüber links des Kastens hingegen\n\
zeigt alle Details.\n",
    12 : \
"Das Foto der Umgebungskarte.\n\
Die Karte ist scharf und detailliert zu erkennen.\n",
    13 : \
"Ein Standard Auto-Verbandkasten.\n\
Nicht ganz klar, ob das jetzt bei einem Tagesausflug zu Fuß noch dem Credo\n\
'Vorsicht ist die Mutter der Porzellankiste' entspricht oder glattweg\n\
in die Schublade 'Panisch und übertrieben vorsichtig' fällt...\n",
    14 : \
"Wahnsinn, was Hunger im Einkaufsladen anrichten kann!\n\
Eure Rucksäcke platzen fast vor Zutaten für eine wahre Picknick-Orgie.\n\
Wenn Ihr das alles esst, werdet Ihr wohl kaum weiterwandern wollen ;)\n",
    15 : \
"Ein kleines Fläschchen Sonnencreme, das Ihr von zu Hause mitgenommen habt,\n\
um in der Sonne nicht auszudörren wie Rosinen.\n", #bonus item
    # 16 : Start bonus 2
    17 : \
"Blütenblätter der Heckenrose. Einige Insektenarten hassen ihren Duft.\n",
    18 : \
"Waldbrombeeren. Lecker. Keine Angst, sie werden euch schon nicht krank machen\n\
oder einem Fuchsbandwurm als Heimat dienen\n",
    19 : \
"Eine Sprühflasche mit Fensterreiniger, die vergessen worden sein muss.\n\
Die Fenster sind jedenfalls sauber!\n",
    20 : \
"Eine Sprühflasche mit einem Rest Fensterreiniger, gefüllt mit Blüten.\n\
Der Alkohol des Reinigers scheint den Blütenblättern den Duft\n\
zu entziehen, denn die leicht undichte Flasche riecht jetzt sehr stark\n\
nach Heckenrose.",
    21 : \
"Ein silberner Schlüssel mit Anhänger aus Metall. Nach gründlicher Reinigung\n\
im trüben Wasser des Sumpfes könnt ihr lesen,\n\
was darauf eingraviert ist: 'S.M. JGU MZ 09'\n",
    22 : \
"Eine SD-Karte, die Ihr dem Seismographen entnommen habt.\n\
Vielleicht solltet Ihr die jemandem bringen, der etwas damit anfangen kann?\n",
    23 : \
"Eine SD-Karte. Darauf steht 'Laacher See, LAS-4'.\n\
Kein Zweifel, diese Karte muss aus der Boje stammen!\n",
    24 : \
"Ein alter, kaputter Schraubendreher. Sein Griff ist gesplittert und\n\
seine Schlitz-Klinge ist so abgenutzt, dass er wohl keine Schraube mehr richtig\n\
greifen kann.\n",
    100 : \
"Eine Bahnstation in der tiefsten Eifel...\n\n",
    101 : \
"Eine große, ziemlich detaillierte Karte der Umgebung in einem\n\
etwas ramponiert aussehendem Glaskasten.\n\
Die Sonne spiegelt sich so sehr darin, dass man kaum etwas erkennen kann.\n\
Ihr Titel: 'Die V_____eifel: Mend__ ___ ____bung, 1:10000'\n\n",
    102 : \
"Der linke Pfosten des Glaskastens.\nEr trägt zwar Rostspuren,\n\
scheint aber grundsolide und tief im Boden verankert.\n\n",
    103 : \
"Die 'Adler-Apotheke' in Mendig. Kennste eine, kennste alle...\n\n",
    104 : \
"Ein REWE-Markt, ziemlich groß für diese Gegend.\n\
Der hat bestimmt alles, was man vergessen haben könnte.\n\n",
    105 : \
"Die große Karte der Umgebung ist jetzt verschattet, da jemand von Euch\n\
vor dem Pfosten steht. Man kann die Karte jetzt klar und deutlich erkennen.\n\n",
    110 : \
"Der Fußweg zu eurem ersten Etappenziel Maria Laach.\n\
Ihr wolltet ungern an der Landstraße entlang gehen und habt Euch für diesen\n\
zugewachsenen, schmalen Pfad entschieden,\n\
den das Wild sicher auch als Weg benutzt. Die Sonne blinzelt immer wieder\n\
durch das Blätterdach, es duftet nach Heckenrosen und ab und zu erhascht Ihr\n\
einen Blick auf den Wald.\n\
Schließlich gelangt Ihr an eine Weggabelung in einer kleinen Senke.\n\
Der Wegweiser wird den letzten Winter wohl nicht überlebt haben,\n\
sein abgebrochener Stumpf ragt ein paar Zentimeter aus dem Boden.\n\n",
    111 : \
"Tiefe Wühlspuren im Gras links und rechts des Weges deuten darauf hin,\n\
dass hier desöfteren Wildschweine auf der Suche nach Nahrung unterwegs sind.\n\
Ihr hofft, dass Ihr keinem Keiler in die Quere kommt und setzt euren Weg\n\
etwas wachsamer fort als vorher.\n",
    112 : \
"Zwischen all dem Gestrüpp seht Ihr zwei Sträucher mit Heckenrosen,\n\
die gerade mit zart pink leuchtenden, duftenden Blüten lockt.\n",    
    113 : \
"Ein Vogelnest mit ein paar Eierschalen drin. Entweder ist\n\
der Nachwuchs bereits aus dem Haus, oder wurde Opfer eines\n\
Räubers.\n",
    114 : \
"Brommbeeren. Dorniges, sehr verwachsenes und undurchdringliches Gestrüpp.\n\
Ein paar fast schwarze, reife Beeren sind für Euch einigermaßen erreichbar\n\
und sehen echt lecker aus.\n",
    115 : \
"Zwischen den Sträuchern öffnet sich plötzlich eine kleine Lücke und gibt\n\
einen noch engeren Pfad frei, der fast im rechten Winkel abzweigt\n",
    120: \
"Nach ein paar hundert Metern sanft bergab verläuft sich der Weg\n\
und endet in lockeren, aber leicht erhöhten, festen Grasbüscheln.\n\
Die Natur hat Euch hier förmlich verschluckt.\n\
Doch - halt - was glitzert da hinten im Gras?\n\n",
    121 : \
"Hier ist es ziemlich nass überall. Obwohl alles mit Gras und Heide\n\
bewachsen ist, steht fast alles ein paar Zentimeter unter Wasser\n\
bis auf ein paar Grasbüschel, die sich wie Inseln über dem\n\
Wasserspiegel befinden und etwa in Schrittweite zueinander wachsen.\n",
    122 : \
"Das typisch-braune, saure Wasser eines Sumpfes. Da der Boden nur aus Pflanzen\n\
und Wasser besteht, gibt er recht stark nach und Ihr sinkt mit jedem Schritt\n\
etwas ein.\n",
    123 : \
"Waargh, Mücken! Dort hinten seht Ihr einen richtigen Schwarm davon.\n",
    124 : \
"Ihr steht zwischen verrosteten Gleisen, die sich mit Weichen in der Ferne\n\
verästeln und im Nebel verschwrinden. Vereinzelt stehen noch Loren herun,\n\
Eine Lok entdeckt Ihr nirgendwo.\n",
    125 : \
"Ihr nähert Euch dem Gegenstand auf dem Boden, doch plötzlich ist\n\
das Glitzern verschwunden.\n\
Nach längerer Suche ein paar Schritte vor und zurück ist das Glitzern\n\
plötzlich wieder da. Doch nähert Ihr Euch, verschwindet es wieder.\n",
    126 : \
"Nebel. Keine hundert Meter von Euch entfernt, wirkt die Nebelbank\n\
durchdringlich wie eine Wand.\n",
    127 : \
"Ihr betretet eine große Betonplatte. In ihrer Mitte steht, mit dem Boden\n\
fest verschraubt, ein Zylinderförmiges Metallding auf drei Beinchen.\n\
Es ist nicht sehr hoch, und sein Durchmesser ist etwa so groß wie ein\n\
Suppenteller. Auf einer Seite seht Ihr ein Bedienpanel, an dem eine rote\n\
Leuchtdiode hektisch blinkt. Hinter dem Gerät steht eine große, schwarze Kiste.\n\
Aus einem Loch an ihrer Seite steigt ein weißes Dampffähnchen empor.\n\
Sie ist mit dem Metallding durch eine Leitung verbunden.\n\
Eine weitere, viel dickere Leitung führt von der Kiste zum Leitstand.\n",
    128 : \
"Eine alte Leitwarte für technische Geräte oder so etwas.\n\
Könnte früher mal zur Bahnanlage gehört haben, allerdings steht in der Ecke\n\
vor einem großen Fenster ein Bedienpult neuerer Bauart, als das Alter\n\
der Bahnanlage vermuten lässt.",  #[hidden]
    129 : "Ein ziemlich großes Gerät aus Metall, fast mannshoch und ebebnso\n\
breit. Von hier aus führen einige dicke Leitungen direkt in den Nebel.\n",
    130: \
"Hier geht es eindeutig bergauf. Nicht, dass Ihr das am Gelände sehen könnt,\n\
nein, dafür ist das Unterholz viel zu dicht, aber es ist irgendwie...\n\
anstrengend und wird eher noch anstrengender. \n\
Vorne seht Ihr eine Lichtung, vielleicht gut für eine Rast?\n\n",
    131 : \
"Unten erstreckt sich ein kleiner Sumpf mit vielen alten, toten Bäumen\n\
und mehreren brackigen Wasserflächen. Gen Horizont erstreckt sich\n\
eine Nebelbank, sodass Ihr dort nicht mehr erkennen könnt.\n",
    132 : \
"Ein See glitzert ruhig in der Sonne, umsäumt von einer sanft\n\
ansteigenden Hügelkette. Ihr seht einen kleinen Anleger mit\n\
daran festgemachten Bötchen. Ein schönes, ruhiges Bild und\n\
Ihr bekommt direkt Lust, eine Runde auf dem See zu drehen.\n",
    133 : \
"Mendig aus der Ferne.",
    134 : \
"Die Abtei 'Maria Laach'. Nicht weit von hier, schön gelegen\n\
am Feldesrand, ist sie sicher einen Besuch wert.\n",
    135 : \
"Heiter mit einzelnen Schäfchenwolken. Kein Lüftchen regt sich.\n\
Ein herrlicher Tag für so einen Auslug.\n",
    136 : \
"Eine einfache Parkbank. Sie lädt euch zum Entspannen und Energie tanken ein.\n",
    140 : \
"Das Seeufer. Der See liegt tiefblau und träge da, winzige Wellen plätschern\n\
am schmalen Steinstrand und ein Steg ragt ein paar Meter in den See hinein.\n\
An ihm sind ein paar weiße Tretboote vertäut.\n\
Merkwürdigerweise ist hier kein Tier zu sehen, weder Schwäne noch Enten könnt\n\
ihr ausmachen. Dass hier auch weit und breit keine Menschenseele ist,\n\
stört euch allerdings nicht weiter.\n",
    141 : \
"Ein schmaler Streifen Steinstrand am Rande des Sees. Hier liegt alles herum,\n\
von Kieselsteinen bis hin zu Findlingen. Ihr werft ein paar Steinchen\n\
und seht zu, wie sich die Wasseroberfläche kräuselt.\n",
    142: \
"Am Steg sind ein paar kleine, weiße Tretboote angebunden.\n\
Es ist niemand zu entdecken, der sie euch ausleihen könnte, aber\n\
an einem Poller des Stegs hängt eine kleine Metalldose mit Vorhängeschloss\n\
und der Aufforderung, für die Nutzung eines Bootes doch bitte 5€ zu spenden.\n",
    143 : \
"Eine Metalldose mit einem Schlitz an der Seite und einem Vorhängeschloss.\n\
Jemand hat sie auf der Unterseite mit einem Dosenöffner geöffnet und ausgeleert.\n\
Was für ein trauriges Bild.\n",
    150 : \
"Ihr befindet Euch jetzt mit dem Boot mitten auf dem See.\n\
Das Wetter ist herrlich und die Sonne knallt. Was wollt ihr mehr?\n",
    151 : \
"Das Ufer des Sees ist von Bäumen gesäumt. Ringsherum geht das Terrain bergauf,\n\
sodass ihr den Eindruck bekommt, in einem Suppenteller unterwegs zu sein.\n\
Es ist wirklich sehr still hier und kein Windhauch regt sich. Die Sonne hat\n\
trotz der fortgeschrittenen Jahreszeit noch ordentlich Kraft und bald ist Euch\n\
ziemlich warm, sodass Ihr Euch Eurer Jacken und Pullover entledigt.\n",
    152 : \
"Frisch tretet Ihr in die Pedale und fahrt raus auf den See.\n\
Das Wasser gluckert und schmatzt am Schaufelrad und nach ein paar Manövern\n\
mit dem Ruder habt Ihr das Boot gut unter Kontrolle. Ihr gleitet auf dem Wasser\n\
hin zur Mitte des Sees und spürt den leichten Fahrtwind angenehm im Gesicht.\n",
    153 : \
"Euch fallen ein paar größere Blasen auf, die um Euer Boot herum aufsteigen.\n\
Ein Fisch oder ein Taucher? Schnell fahrt ihr weiter, als ihr bemerkt,\n\
dass die Luft hier plötzlich faulig riecht.\n",
    154 : \
"In der Ferne seht ihr eine silbrige, recht unförmige Boje\n\
aus dem Wasser ragen. Sie ist mit gelb-schwarzen Aufklebern versehen,\n\
die Ihr aus der Entfernung aber nicht entziffern könnt.\n",
    155 : \
"Na ja, die Sonne, die brennt Euch ganz schön auf den Pelz. Habt Ihr bei solchen\n\
Ausflügen normalerweise Sonnencreme dabei?\n",
    160 : \
"Ihr seid bei der Boje angekommen. Aus der Nähe wirkt sie sogar noch komischer.\n\
Sie ist aus silbernem Stahl und mit Solarzellen bestückt.\n\
Von Nahem erinnert ihre Form nicht mehr so sehr an ein Ei, denn sie scheint\n\
komplett aus dreieckigen Stahlteilen gefertigt und sieht sehr futuristisch aus.\n\
Sie hat einen Poller, wo man Boote festmachen kann und sieht so aus, als wäre sie\n\
in letzter Zeit oft besucht worden.\n\
Ihr macht Euer Boot fest und beschließt, hier eine kurze Pause einzulegen.\n",
    161 : \
"Die Sonne brennt gnadenlos auf Euch nieder.\n",
    162 : \
"Euer Boot ist sicher an diesem Poller verzurrt. Ein an der Boje angebrachter\n\
Gummipuffer quietscht, wenn ihr Euch auf Eurem Boot bewegt.",\
    163 : \
"Die Wartungsklappe der Boje. Normalerweise wäre sie per Schlüssel\n\
zu öffnen, doch die Schrauben, die das Schloss halten sind so locker,\n\
dass das Schloss auf der Innenseite der Klappe verrutscht sein muss.\n\
Jemand hat offensichtlich bereits versucht, die Klappe mit Gewalt zu öffnen,\n\
denn überall sind Kratz- und Hebelspuren zu sehen.",
    164 : \
"Das Display der Boje. An der Ecke, die der Wartungsklappe am nächsten liegt,\n\
ist es gerissen, sodass ein Großteil nicht mehr ablesbar ist.\n\
Zu erkennen sind folgende Meldungen:\n\
'No Cell'\n\
'___Card Error'\n\
'Implausible ______ from Sens___ H2SO__1'\n\
'Power ______ OK'\n",
    165 : \
"Ein leerer SD-Kartenschlitz.",
    170  : \
"Der Pfad am See führt Euch erneut in den Wald. Bald schon geht ihr auf\n\
weichem Laub und trockenen Ästen, und wo der Wald dunkler wird, gibt es auch\n\
immer weniger Buschwerk und Unterholz.\n\
Völlig unvermutet taucht am Wegesrand eine Parkbank auf.\n\
Warum hier wohl jemand so etwas hinstellt?\n",
    10101: \
"Ihr nehmt ein Foto der Übersichtskarte auf, um es Euch später ansehen zu können.\n\
Gute Idee!\n",
    10105: \
"Ihr nehmt ein Foto der Übersichtskarte auf, um es Euch später ansehen zu können.\n\
Gute Idee!\n"
    }

#Defines what happens on closer investigation or usage of an item
dictAction = {
    13: \
"Ihr beschließt, den Verbandkasten zu benutzen, um eure Wunden\n\
und die eurer möglichen Begleiter zu versorgen. Das funktioniert prima!\n\
(Euch ist natürlich klar, dass das jetzt nur einen Effekt hatte,\n\
wenn Ihr auch wirklich verletzt wart. Sonst sieht es einfach nur albern aus,\n\
in Rettungsdecke und mit Verbänden und Pflastern übersät herumzulaufen)\n",
    14: \
"Jetzt ein Picknick! Ihr lasst Euch auf der mitgebrachten Decke nieder und genießt\n\
ein fürstliches Mahl in der Natur. Auch wenn Ihr jetzt wieder motivierter seid,\n\
euren Ausflug fortzusetzen, so hat Euch das viele Essen doch ein Kantinenkoma beschert.\n",
    15 : \
"Ihr cremt Euch gut ein. Der Duft erinnert Euch an Euren letzten Sommerurlaub.\n",
    18: \
"Süß-sauer sind die Brombeeren. Sie schmecken viel besser als die, die man ohne\n\
dafür gekämpft zu haben im Supermarkt kaufen kann.\n",
    101 : \
"Der Kartenausschnitt scheint perfekt zu eurer geplanten Tour zu passen,\n\
nur leider könnt Ihr wegen der Spiegelung im Glas nichts Genaues erkennen.\n",
    102 : \
"Du stehst am Pfosten des Kartenkastens.\n\
An dieser Position schattest du den Kartenkasten ab,\n\
sodass die Karte einwandfrei lesbar ist.\n",
    103 : \
"Ihr betretet die Apotheke. Warum, das ist Euch selbst noch nicht ganz\n\
klar geworden, als Euch schon ein freundlicher Herr hohen Alters mit Haarkranz,\n\
goldener Brille und weißem Kittel - ganz nach dem Klischee - anspricht.\n\
Aus Verlegenheit kauft Ihr einen Verbandkasten.\n\
Tja, dieses sperrige Stück muss nun den ganzen Weg mitgeschleppt werden.\n",
    104 : \
"Hach, ganz wie zu Hause! So eine Zugfahrt macht echt hungrig, und so\n\
kauft Ihr, obwohl Ihr Euch natürlich ein paar Brote geschmiert habt, einen\n\
ganzen Haufen Lebensmittel zusammen. Wohl bekomm's!\n\
Nur leider ist so ein Einkauf auch immer etwas anstrengend...\n",
    105 : \
"Die Übersichtskarte ist jetzt perfekt lesbar.\n",
    112 : \
"Hmmm, wie die Heckenrosen duften!\n\
Das werden allerdings nicht alle Insektenarten so sehen...\n\
Schnell pflückt Ihr ein paar der duftenden Blütenblätter und steckt sie ein.\n",
    114 : \
"Wilde Brombeeren. Immer eine Tortur, sie zu pflücken,\n\
denn nicht nur einmal bleibt Ihr an Dornen hängen und reißt Euch die Haut auf.\n\
Dafür sehen sie aber so gut aus, dass Euch das Wasser im Mund zusammenläuft.\n", 
    115 : \
"Der Pfad schlängelt sich, immer enger werdend, noch eine Weile geradeaus\n\
und biegt dann scharf nach links ab. Hier gibt es immer mehr Dornengestrüpp\n\
und durch das dichte Blätterdach dringt kaum mehr ein Sonnenstrahl.\n\
Vergeblich sucht Ihr nach Wegmarkierungen und Zeichen, bis Ihr schließlich\n\
vor einer hohen Steinwand steht, wo der Weg abrupt zu enden scheint.\n\
Hier kommt wohl nur Wild durch, was sich gut im Gebirge bewegen kann.\n\
Ihr beschließt, lieber umzukehren und einen besser zu wandernden Weg\n\
zu wählen.\n",
    121 : \
"Schon ist es passiert. Da bewundert man die Natur und konzentriert\n\
sich einmal nicht genau darauf, die Grassoden auch genau zu treffen,\n\
und schon hängt ein Fuß im Morast. Sehr zur (Schaden)Freude anderer,\n\
ruderst Du ein paar Sekunden lang hilflos mit den Armen,\n\
bevor Dir geholfen wird und Du Deinen Fuß dem Sumpf mit einem lauten \n\
Schmatzgeräusch entreißen kannst.\n",
    122 : \
"'Das ist ja eine Brühe', denkst Du, und schon\n\
steckst Du bis zur Kniekehle drin. Klasse!\n\
Dummerweise wird Dein Rucksack nass, sodass Ihr befürchten müsst,\n\
dass Gegenstände unbrauchbar geworden sind.\n",
    123 : \
"Mücken, viele Mücken, das wisst Ihr ja schon. Ihr wagt nicht,\n\
Euch dem Schwarm weiter zu nähern - Er würde Euch schier aussaugen.\n\
Direkt hinter dem Mückenschwarm seht Ihr eine kleine Baracke.\n\
Sie scheint noch vor Kurzem benutzt worden zu sein, denn anders\n\
als die Gleisanlage sieht sie recht gut in Schuss und sauber aus.\n",
    124 : \
"Die alte Gleisanlage deutet darauf hin, dass in dieser Gegend früher\n\
Torf gestochen wurde. Sie muss seit langer Zeit außer Betrieb sein, denn\n\
einige Gleise sind im weichen Boden versackt und die Loren sehen so verrostet\n\
aus, als würden sie jeden Moment auseinanderfallen.\n\
Ihr entscheidet Euch, diesen Ort bald zu verlassen.\n",
    125 : \
"Genau prägt Ihr Euch den Ort des Gegenstandes ein und fixiert ihn.\n\
Euch langsam annähernd, konzentriert Ihr Euch besonders, als das Ding\n\
erneut unter der Wasserobefläche verschwindet, da der Boden unter Eurem\n\
Gewicht nachzugeben scheint. Um den Gegenstand nicht in der Tiefe zu verlieren,\n\
tastet Ihr sehr vorsichtig im kalten, murkigen\n\
Wasser herum, und schließlich habt Ihr ihn in der Hand - \n\
Es ist tatsächlich ein silberner Schlüssel!\n\
Daran fällt ein schlammiger Schlüsselanhänger auf.\n",
    126 : \
"Eine Nebelbank. Hier im Sumpf nichts Besonderes. Euer gesunder\n\
Menschenverstand sagt Euch, dass es ziemlich dumm wäre, da so einfach\n\
ohne Hilfsmittel und ohne konkretes Ziel hinein zu marschieren, denn wenn\n\
man dort schon die Hand vor Augen nicht sehen kann, wie soll man dann\n\
erst erkennen, wo man hintritt?\n",
    127 : \
"Ihr öffnet die Klappe des Bedienpanels. Es hat die Aufschrift 'STS-3'.\n\
Neben einem Speicherkartenschlitz blinkt eine rote Leuchtdiode\n\
mit der Aufschrift: 'Mem Overflow!'. Darunter leuchtet ein gelbes Lämpchen\n\
'No Cellular'. Kurzerhand entschließt Ihr Euch, die Speicherkarte mitzunehmen.\n",
    128 : \
"Unter dem großen Fenster des Leitstandes befindet sich eine Konsole\n\
mit kleinem Display und nur zwei Knöpfen sowie einem Lämpchen\n\
und einem Schlüsselschalter.\n\
Die Beschriftungen sind zum Teil verrottet, dennoch könnt Ihr die Worte 'Fan'\n\
und 'Stack health' entziffern. Das Display darüber zeigt blass '08%' an.\n\
Auf dem Boden liegen ein offensichtlich kaputter, rostiger Schraubendreher und\n\
eine Flasche Fensterreiniger, deren Inhalt größtenteils\n\
ausgelaufen sein muss. Ihr nehmt beide Gegenstände mit, um sie im nächsten\n\
Mülleimer zu entsorgen.\n",
    129 : \
"Das Gerät besitzt hinten zwei geschlitzte Öffnungen,\n\
ähnlich wie Lüftungsöffnungen an Gebäuden. Vorne befindet sich ein Gitter.\n\
Im Halbdunkel dahinter steckt eine Rolle mit Lamellen drauf, so breit wie\n\
der Kasten selbst. Durch das Maschinenetikett 'Main Blower' kommt Ihr\n\
zu dem Schluss, dass es sich bei dem Gerät um ein Gebläse handeln muss.\n",
    136 : \
"Aaaaah, eine Pause. Tut echt gut, wenn man ein wenig müde ist.\n\
Lümmelt nur nicht zu viel hier herum, sonst habt Ihr bald keine\n\
Lust mehr, überhaupt noch weiter zu gehen.\n",
    142 : \
"Ihr beschließt, eine Runde auf dem See zu drehen.\n\
Das kleine Bötchen schwankt stark, als ihr es betretet.\n\
Es gibt hier zwei Sitzplätze zum Treten und zwei weitere erhöht achtern,\n\
von denen aus man einen tollen Rundumblick hat.\n\
Zwischen den Vordersitzen befindet sich eine runde Erhöhung, in der sich\n\
das Schaufelrad befinden muss. Links und rechts an der Seite befestigt ist\n\
das Rudergestänge für die Steuerung.\n\
Vorsichtig fahrt ihr los, mitten auf den See hinaus. Das klappt echt prima!\n",
    153 : \
"Ihr wollt die Blasen genauer untersuchen, aber viel sieht man auch bei direktem\n\
Blick nach unten nicht. Ins Wasser gehen möchte jetzt auch keiner so wirklich.\n\
Allmählich bekommt Ihr Kopfschmerzen und der Geruch wird unerträglich,\n\
sodass Ihr beschließt, abzudrehen.\n",
    154 : \
"Die Boje sieht ziemlich plump aus. Sie ist fast eiförmig und am oberen Ende\n\
steckt eine Kugel an einer Stange. Auf ihrer Außenhaut sind mehrere dunkle\n\
Rechtecke zu sehen.\n",
    155 : \
"Klasse, zum Glück habt Ihr Sonnencreme eingepackt. Als hättet Ihr es geahnt!\n\
Die könnt Ihr ja dann direkt mal benutzen ;)\n",
    161 : \
"Wenn ihr bis jetzt keine Sonnencreme auftragen konntet, ist es zu spät\n\
und Ihr bekommt einen fetten Sonnenbrand.\n",
    163 : \
"Die bekommt ihr so niemals auf. Wahrscheinlich ist sie nicht nur verschlossen,\n\
sondern durch den Aufbruchversuch auch total verklemmt.\n\
Warum wollt ihr die Klappe überhaupt öffnen?\n",
    15123 : \
"Whow, ihr seid aber gut vorbereitet! Zack, Mückenspray auf Mücken angewendet -\n\
gut, es mag unkonventionell sein, sich nicht selbst damit einzureiben -\n\
und schon sind sie weg und Euer Weg ist frei!\n", #TODO implement feature ItemSpotAction in GameMech!
    20123 : \
"Na dann mal sehen, was euer Parfum bei den Mücken ausrichten kann!\n\
Ein paar Sprühstöße hier, da - und - weg sind die Mücken!\n\
Ganz klar ist Euch allerdings nicht, ob das jetzt an den Heckenrosen lag\n\
oder doch an der Chemie des Fensterreinigers. Sei's drum. Euer Weg ist frei.\n",
    21128 : \
"Der Schlüssel passt! Beherzt dreht ihr den jetzt freigegebenen Schalter.\n\
Das Bedienpanel erwacht zum Leben und ein Lämpchen über einem grünen Knopf\n\
beginnt weiß zu blinken.\n\
Ihr drückt den Knopf.\n\
Ihr drückt den Knopf erneut, fester.\n\
Mit einem gewaltigen Heulen läuft die Maschine gegenüber des Leitstandes an\n\
und nach ein paar Sekunden rauscht sie monoton vor sich hin.\n\
Sie scheint die Nebelbank allmählich aufzulösen.\n\
Noch bevor sie komplett verschwindet, fällt die Maschine plötzlich aus.\n\
Das Display zeigt die 'Stack health' jetzt mit '00%' an.\n",
    22163 : \
"Anstatt die Klappe aufzuhebeln, versucht Ihr zuerst, das Schloss wieder\n\
ordentlich festzumachen. Als ihr fast fertig seid,\n\
rutscht Euch der Schraubenzieher ab und fällt ins Wasser, aber nicht, bevor\n\
sich ein Splitter vom Griff löst und sich in Eure Hand bohrt.\n\
Wütend schlagt ihr auf die Wartungsklappe, die mit einem leichten Quietschen\n\
prompt aufspringt.\n"

    }

    
#Defines room number and names
dictRooms = {
    100 : "Bahnhof Mendig",\
    110 : "Fußweg Maria Laach",\
    120 : "Sumpf im Wald",\
    130 : "Der Hügel vor dem Bergkamm",\
    140 : "Seeufer",\
    150 : "Auf dem See",\
    160 : "An der Boje",\
    170 : "Parkbank im Wald",\
    180 : "Abtei Maria Laach",\
    190 : "Teufelskanzel",\
    200 : "Krufter Waldsee",\
    210 : "vor dem Lager"\
    }

#Defines which rooms are in what way connected to which rooms
dictConnectedRooms = {
    100 : [110],\
    110 : [100, 120, 130],\
    120 : [110],\
    130 : [110, 140],\
    140 : [130, 150, 170],\
    150 : [140, 160],\
    160 : [140, 150],\
    170 : [140, 180],\
    180 : [170, 190],\
    190 : [180, 200],\
    200 : [210]\
    }

#Defines spot number and names
#hidden:
#105 at 102,
#125 at 123,
#127 at 126
dictSpots = {
    101 : "die Übersichtskarte",\
    102 : "der Pfosten eines Kartenkastens",\
    103 : "die Apotheke am Bahnhof",\
    104 : "der REWE-Markt",\
    105 : "die Übersichtskarte, verschattet",\
    111 : "Wühlspuren",\
    112 : "Heckenrosen",\
    113 : "Vogelnest",\
    114 : "Brommelbeeren",\
    115 : "Weiter den Pfad entlang...",\
    121 : "Grassoden",\
    122 : "Bräunliches Wasser",\
    123 : "Mücken...",\
    124 : "Gleisanlage mit Loren",\
    125 : "Das glitzernde Ding...",\
    126 : "Nebelbank",\
    127 : "Seismograph",\
    128 : "Gerätestand",\
    129 : "Großes, schweres Metallding",\
    131 : "Sümpfe im Nebel",\
    132 : "See hinterm Berg",\
    133 : "Die Stadt",\
    134 : "Die Abtei",\
    135 : "Wetter...",\
    136 : "Pause?",\
    141 : "Strand",\
    142 : "Tretboote am Steg",\
    143 : "Kleine Spardose aus Metall",\
    151 : "Ufer und Bäume",\
    152 : "Raus auf den See",\
    153 : "Blubberblasen",\
    154 : "Merkwürdige Boje",\
    155 : "Euer Rucksack",\
    161 : "Das Wetter...",\
    162 : "Poller zum Festmachen",\
    163 : "Wartungsklappe",\
    164 : "Display",\
    165 : "SD-Kartenschlitz"\
    
    }

#Defines what happens if a closer investigation of spot is refused
dictActionRefused = {
    # TODO
    }

#Action type of the spot when visited
#yields:
#101 11
#105 12
#112 17
#114 18
#125 21
#128 19, 22
#Spots that are not mentioned here, don't have an "advanced" action
dictActionType = {
    101 : Action_id.VIEW,\
    102 : Action_id.NOC_YES,\
    103 : Action_id.GOTO,\
    104 : Action_id.GOTO,\
    105 : Action_id.VIEW,\
    111 : Action_id.NOC_YES,\
    112 : Action_id.VIEW,\
    114 : Action_id.GET,\
    115 : Action_id.GOTO,
    121 : Action_id.NOC_YES,\
    122 : Action_id.NOC_YES,\
    123 : Action_id.VIEW,\
    124 : Action_id.VIEW,\
    125 : Action_id.VIEW,\
    126 : Action_id.VIEW,\
    127 : Action_id.GET,\
    128 : Action_id.USE,\
    129 : Action_id.GOTO,\
    136 : Action_id.USE,\
    142 : Action_id.USE,\
    153 : Action_id.VIEW,\
    154 : Action_id.VIEW,\
    155 : Action_id.OPEN,\
    161 : Action_id.NOC_YES,\
    163 : Action_id.OPEN\
    }    

#Defines how spots are connected to items   
dictSpotItems = {
    10101 : [11],\
    103 : [13],\
    104 : [14],\
    10105 : [12],\
    112 : [17],\
    114 : [18],\
    128 : [19,22],\
    125 : [21],\
    155 : [15],\
    1719 : [20]\
    }
    
#Special items
#dictSpecialItems = {
#123 : [20,15,"Tja, scheinbar habt ihr ] \
#}

#Defines which spots can change through interaction
#with spot or item combination
# Trigger : [[Exchange targets], [Exchange spots]]
dictSpotChange = {
    102: [[101], [105]],\
    15123: [[123], [125]],\
    20123: [[123], [125]],\
    21128: [[126], [127]],\
    22163: [[163], [164, 165]]\
    }

#Defines item number and names
#bonus items (ask player) TODO IMPLEMENT
#15
dictItems = {
    10 : "Ein Smartphone",\
    11 : "Ein Foto der Umgebungskarte",\
    12 : "Ein Foto der Umgebungskarte",\
    13 : "Ein Verbandkasten",\
    14 : "Eine ordentliche Mahlzeit",\
    15 : "Sonnencreme",\
    17 : "Duftende Blütenblätter",\
    18 : "Eine Handvoll Brombeeren",\
    19 : "Sprühflasche",\
    20 : "Heckenrosen-Parfum",\
    21 : "Schlüssel mit Anhänger",\
    22 : "SD-Karte aus dem Seismographen",\
    23 : "SD-Karte aus der Boje",\
    24 : "Defekter Schraubendreher",\
    
    }

#Items that are deleted when player triggers action.  
dictItemDelete = {
    122 : [18, 22],\
    161 : [15],\
    }

#Defines item modifiers
# [0] = motivation, [1] = tiredness
dictMods = {
    11 : [0,-1],\
    12 : [1,1],\
    13 : [3,-1],\
    14 : [5,-2],\
    15 : [2,0],\
    18 : [2,0],\
    104 : [0,-1],\
    103 : [-1,0],\
    108 : [-1,0],\
    111 : [0,1],\
    115 : [0, -2],\
    121 : [-1,0],\
    122 : [-2,0],\
    136 : [1,3],\
    153 : [0,-2],\
    161 : [-2,0],\
    22163 : [-2,0],\
    }

dictModType = {
    10 : Mod_typ.PERMANENT,\
    11 : Mod_typ.NOTUSABLE,\
    12 : Mod_typ.PERMANENT,\
    13 : Mod_typ.EFFALL,\
    14 : Mod_typ.EFFALL,\
    15 : Mod_typ.EFFALL,\
    16 : Mod_typ.NOTUSABLE,\
    18 : Mod_typ.EFFONE,\
    21 : Mod_typ.NOTUSABLE,\
    104 : Mod_typ.EFFONE,\
    103 : Mod_typ.EFFONE,\
    108 : Mod_typ.EFFONE,\
    111 : Mod_typ.EFFALL,\
    115 : Mod_typ.EFFONE,\
    121 : Mod_typ.EFFONE,\
    122 : Mod_typ.EFFALL,\
    136 : Mod_typ.EFFALL,\
    153 : Mod_typ.EFFALL,\
    22163 : Mod_typ.EFFALL\
    }

dictModsRefused = {
    #TODO: add
    }

class GameMsg():
    ASKCONT = "Möchtet Ihr Euer aktuelles Spiel (falls vorhanden) fortsetzen?\n"
    SUCCESS = "...erfolgreich!\n"
    LOAD = "Lade Spielstand..."
    ASKOVWR = "Möchtet Ihr Euren alten Spielstand (falls vorhanden) überschreiben?\n"
    NAN = "Keine Zahl erkannt. Zum Speichern und Beenden bitte 'quit' eingeben.\n"
    SVQT = "Spiel wird gespeichert und beendet. Bis bald!\n"
    TURN = [" bei [", "] ist an der Reihe.\nWas wollt Ihr tun?  "]
    IN_REACH = "\nVon hier aus sind folgende Orte erreichbar:\n"
    NOT_IN_REACH = [" ist von hier aus\n", " leider nicht erreichbar...\n"]
    YOURE_AT = ["Ihr befindet Euch bei ", ".\n\nIhr seht:\n"]
    UNKNOWN_ROOM = ": ???\n"
    EXAMINE = "Ihr untersucht: "
    ACTIONQ = "Möchtet Ihr "
    ACTIONP = "Bitte eingeben: JA: '1', NEIN: '0'.\n"
    ACTIONE = "Ja, manchmal ist es auch gut, Dinge NICHT zu tun.\n"
    USED = " wurde verbraucht.\n"
    CANT_USE = " kann nicht allein benutzt oder verbraucht werden.\n"
    MUST_COMB = "Dieser Gegenstand kann nicht ohne Kombination benutzt werden.\n"
    CANT_CMB = "Das lässt sich nicht kombinieren!\n"
    NOT_INV = "Dafür müsstet Ihr das erstmal auch alles im Inventar haben...\n"
    UNKNOWN_CMD = "Kein bekanntes Kommando.\n"
    SUCCESS_GET = "Das war erfolgreich! Ihr erhaltet "
    CHMOD = [", dein Wohlbefinden ändert sich um:\nMotivation: ", "\nMüdigkeit: "]
    LOADING = "______________________________________________________________________\n"
    LOOSE = "Ihr verliert "
    NO_SVGAME = "Fehler: Keinen Spielstand zum Laden gefunden.\n\
Beginne neues Spiel.\n"
    TIRED = ", du bist müde. Hundemüde. Sieh' zu, dass Du Dich schnleunigst ausruhst!\n\
In so einem Zustand verlierst Du langsam Deine Motivation............................\n"
    UNMOT = [", du hast im Moment echt gar keinen Bock mehr auf diesen Ausflug,\n\
Dir geht alles einfach nur auf den Keks.\n\
Ihr solltet an dieser Stelle einfach mal eine Pause machen.\n",
", möchtest Du ", " mit einem 'Och komm' schon' oder einer anderen\n\
Form der flammenden Motivationsansprache helfen und ", "\n\
die Hälfte Deiner Motivation abgeben?\n"]
    UNMOT_END = "Puh, es hilft alles nichts. Ihr macht jetzt erstmal schön eine Pause.\n\
Später - sagen wir ab in einer halben Stunde - könnt Ihr dann mit frischer\n\
Motivation weitermachen........................................................\n"