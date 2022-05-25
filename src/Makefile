translate-create-pro:
	echo -n "SOURCES = " >messages/translate.pro
	find messages/.. -name \*py | sed 's/messages\///' | xargs echo -n >>messages/translate.pro
	echo "" >>messages/translate.pro
	echo -n "FORMS = " >>messages/translate.pro
	find messages/.. -name \*ui | sed 's/messages\///' | xargs echo -n >>messages/translate.pro
	echo "" >>messages/translate.pro
	echo "TRANSLATIONS    = hu_HU.ts" >>messages/translate.pro
	echo "" >>messages/translate.pro

translate-update:
#	lupdate . -ts messages/hu_HU.ts -no-obsolete
#	pylupdate5 messages/translate.pro
	pyside2-lupdate -verbose messages/translate.pro
translate-lrelease:
	lrelease messages/hu_HU.ts