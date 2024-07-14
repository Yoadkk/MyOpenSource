import tkinter as tk
import random

# רשימת המילים, הפירושים ושאלות אמריקאיות
words = [
    {"word": "אנכרוניסטי", "meaning": "מיושן, שייך לתקופה אחרת"},
    {"word": "אקסיומה", "meaning": "הנחה שאין לערער עליה, אמיתה"},
    {"word": "בוסר", "meaning": "פרי לא בשל, דבר שלא הגיע להבשלתו המלאה"},
    {"word": "דיסוננס", "meaning": "חוסר הרמוניה, ניגוד צורם"},
    {"word": "היפותטי", "meaning": "משוער, דבר שניתן להניחו אך אינו ודאי"},
    {"word": "וירטואוז", "meaning": "אדם המצטיין בתחומו, במיוחד במוזיקה או באמנות"},
    {"word": "טרנסצנדנטי", "meaning": "על טבעי, נעלה על כל חוויה אנושית"},
    {"word": "לאקוני", "meaning": "תמציתי, קצר ולעניין"},
    {"word": "מאניה", "meaning": "מצב של התרגשות יתר, מצב רוח מרומם באופן קיצוני"},
    {"word": "ניחם", "meaning": "חזר בו ממה שעשה, הביע חרטה"},
    {"word": "סובייקטיבי", "meaning": "אישי, תלוי בהשקפה האישית של הפרט"},
    {"word": "פוסטולאט", "meaning": "הנחת יסוד שמקבלים אותה כנכונה לצורך בניית תאוריה"},
    {"word": "קטגוריה", "meaning": "סיווג, קבוצה, מחלקה"},
    {"word": "רטרוספקטיבי", "meaning": "מבט לאחור, בחינה של אירועים מהעבר"},
    {"word": "שוחר", "meaning": "חובב, רוצה, מתעניין במשהו"},
    {"word": "אבחה", "meaning": "חתך מהיר, תנועה מהירה"},
    {"word": "אגוצנטרי", "meaning": "מרוכז בעצמו, חושב רק על טובתו"},
    {"word": "אדוק", "meaning": "קפדן בדתו, מסור לדבר מה"},
    {"word": "אודיסאה", "meaning": "מסע ארוך והרפתקני"},
    {"word": "אוזלת יד", "meaning": "חוסר יכולת לפעול"},
    {"word": "איזמל", "meaning": "כלי חיתוך חד, סכין כירורגית"},
    {"word": "אכיפה", "meaning": "יישום החוק, הבאת החוק לידי מימוש"},
    {"word": "אלגוריה", "meaning": "סיפור עם מוסר השכל, דימוי מורחב"},
    {"word": "אמביוולנטי", "meaning": "בעל רגשות מעורבים, דו ערכי"},
    {"word": "אניגמה", "meaning": "תעלומה, דבר מסתורי"},
    {"word": "אצטבה", "meaning": "מדף, רף"},
    {"word": "באוש", "meaning": "רקוב, מסריח"},
    {"word": "בגדי אדם", "meaning": "בגדים פשוטים, בגדים יומיומיים"},
    {"word": "בוגדני", "meaning": "חסר נאמנות, נבגד"},
    {"word": "בוטה", "meaning": "חריף, תקיף, לא מעודן"},
    {"word": "ביזארי", "meaning": "מוזר, יוצא דופן"},
    {"word": "בית מטבחים", "meaning": "משחטה, מקום שבו שוחטים בהמות"},
    {"word": "גאולוגיה", "meaning": "חקר כדור הארץ, המדע של כדור הארץ"},
    {"word": "גבנון", "meaning": "בליטה, גבעה קטנה"},
    {"word": "גדיש", "meaning": "ערימת תבואה, קציר"},
    {"word": "גלופין", "meaning": "בעל שכרות קלה, שיכור במקצת"},
    {"word": "גמא", "meaning": "בלע, שתה בלגימה אחת"},
    {"word": "דבוקה", "meaning": "קבוצה צמודה של אנשים או חפצים"},
    {"word": "דובב", "meaning": "הביא מישהו לדבר, עורר שיחה"},
    {"word": "דו-קיום", "meaning": "חיים יחד בשלום, שיתוף פעולה"},
    {"word": "דוגמה", "meaning": "אמונה או עיקרון שמקבלים אותו כנכון"},
    {"word": "דינמי", "meaning": "משתנה, פעיל"},
    {"word": "דיפוזיה", "meaning": "תפוצה, פיזור"},
    {"word": "הבזק", "meaning": "הבחה מהירה של אור, ברק"},
    {"word": "הביל", "meaning": "רטוב מאוד, לח"},
    {"word": "הבלחה", "meaning": "הבהוב חלש של אור"},
    {"word": "הגה", "meaning": "חשיבה, מחשבה, רעיון"},
    {"word": "הדהד", "meaning": "החזיר קול, יצר הד"},
    {"word": "הולך שולל", "meaning": "רומה, הונאה"},
    {"word": "הולם", "meaning": "מתאים, מתאים לסיטואציה"},
    {"word": "הומוגני", "meaning": "אחיד, בעל חלקים זהים"},
    {"word": "הונאה", "meaning": "רמאות, שקר"},
    {"word": "הפנמה", "meaning": "הפיכת משהו לחלק מהפנימיות, הפנמת ערכים"},
    {"word": "הצטברות", "meaning": "התגבשות של כמות גדולה, ריכוז"},
    {"word": "הקפדה", "meaning": "שמירה קפדנית, עמידה על כללים"},
    {"word": "הרמוניה", "meaning": "הרמוניה, התאמה בין חלקים שונים"},
    {"word": "השערה", "meaning": "הנחה שמבוססת על סימנים"},
    {"word": "התמרמרות", "meaning": "תחושת כעס ותסכול, טינה"},
    {"word": "התנחשל", "meaning": "גלש, התגלגל"},
    {"word": "התעבות", "meaning": "הפיכה לעבה יותר, הצטברות לחות"},
    {"word": "התפוגג", "meaning": "נעלם, התאדה"},
    {"word": "התרצה", "meaning": "נכנע, הסכים"},
    {"word": "זיבורית", "meaning": "אדמה לא פורייה, קרקע דלה"},
    {"word": "זנח", "meaning": "נטש, עזב"},
    {"word": "חגיגה", "meaning": "אירוע של שמחה, מסיבה"},
    {"word": "חד-משמעי", "meaning": "ברור, לא משתמע לשתי פנים"},
    {"word": "חוכא ואיטלולא", "meaning": "צחוק ולעג"},
    {"word": "חיבוק דוב", "meaning": "חיבוק חזק מדי, שמזיק במקום להועיל"},
    {"word": "חכירה", "meaning": "השכרת נכס לתקופה קצובה"},
    {"word": "חלחלה", "meaning": "פחד עמוק, רעד"},
    {"word": "חרף", "meaning": "על אף, למרות"},
    {"word": "חשדנות", "meaning": "אי אמון, נטייה לחשוד"},
    {"word": "טבולה רסה", "meaning": "לוח חלק, מצב של חוסר ידע מוקדם"},
    {"word": "טרוט", "meaning": "עייף, לא רענן"},
    {"word": "יוקד", "meaning": "בוער, חם מאוד"},
    {"word": "יציע", "meaning": "מקום מוגבה לצפייה, חלק מהאצטדיון"},
    {"word": "יראה", "meaning": "פחד, חרדה"},
    {"word": "כביר", "meaning": "גדול, עצום"},
    {"word": "כבוד", "meaning": "הערכה, הערכה עצמית"},
    {"word": "כהות חושים", "meaning": "חוסר תחושה, חוסר רגישות"},
    {"word": "כיול", "meaning": "התקנה של מכשיר למדידה מדויקת"},
    {"word": "כינוי", "meaning": "שם נוסף, תואר"},
    {"word": "כלים", "meaning": "חפצים לשימוש ביתי, כלים למטבח"},
    {"word": "כלאיים", "meaning": "שילוב של שני מינים שונים"},
    {"word": "כמיהה", "meaning": "רצון עז, תשוקה"},
    {"word": "לאות", "meaning": "עייפות, תשישות"},
    {"word": "לבחוש", "meaning": "לערבב, לערבל"},
    {"word": "להיטות", "meaning": "התלהבות, רצון עז"},
    {"word": "להנחות", "meaning": "לכוון, להדריך"},
    {"word": "לזרוק", "meaning": "להשליך, להעיף"},
    {"word": "לחם חוק", "meaning": "משהו קבוע, הכרחי"},
    {"word": "לטושה", "meaning": "מבריקה, חלקה"},
    {"word": "להקת", "meaning": "קבוצת אנשים שמנגנת או שרה יחד"},
    {"word": "לשעבר", "meaning": "שהיה בעבר, לשעבר"},
    {"word": "מאובק", "meaning": "מכוסה אבק, מלוכלך"},
    {"word": "מגדל שן", "meaning": "מקום מבודד, לרוב בשימוש לאקדמיה"},
    {"word": "מוטציה", "meaning": "שינוי גנטי, שינוי פתאומי"},
    {"word": "מיובש", "meaning": "חסר מים, יבש"},
    {"word": "מיכל", "meaning": "מיכל לאחסון נוזלים או גזים"},
    {"word": "מיתוס", "meaning": "סיפור אגדי, אגדה"},
    {"word": "מכונה", "meaning": "מכונה, מכשיר"},
    {"word": "מלגה", "meaning": "תמיכה כספית ללימודים, מענק לימודים"},
    {"word": "מלעיל", "meaning": "טונציה גבוהה יותר, בדרך כלל במילה ארוכה"},
    {"word": "מניע", "meaning": "סיבה לפעולה, גורם"},
    {"word": "מעילה", "meaning": "גניבה, שימוש לא ראוי בכספים"},
    {"word": "מעונן", "meaning": "מכוסה עננים, לא בהיר"},
    {"word": "מעפיל", "meaning": "עולה למעלה, מטפס"},
    {"word": "מערכה", "meaning": "קרב, חלק מהמחזה"},
    {"word": "מצוד", "meaning": "חיפוש נמרץ, מרדף"},
    {"word": "מקלט", "meaning": "מקום מחסה, מקום מסתור"},
    {"word": "מרזח", "meaning": "מקום של שמחה, מסבאה"},
    {"word": "מרכול", "meaning": "חנות גדולה, סופרמרקט"},
    {"word": "משוב", "meaning": "תגובה, פידבק"},
    {"word": "משכן", "meaning": "מקום מגורים, דירה"},
    {"word": "משקיף", "meaning": "אדם שצופה, תצפיתן"},
    {"word": "מתירנות", "meaning": "חופש פעולה, חוסר הגבלה"},
    {"word": "נביעה", "meaning": "מקום שממנו פורצים מים, מקור"},
    {"word": "נגע", "meaning": "מחלה, פגע"},
    {"word": "נידח", "meaning": "רחוק, מבודד"},
    {"word": "ניכור", "meaning": "תחושת זרות, ריחוק"},
    {"word": "נמל", "meaning": "מקום עגינה לספינות, נמל ימי"},
    {"word": "נמהר", "meaning": "פזיז, מהיר"},
    {"word": "ניצול", "meaning": "שימוש לרעה, הפקת תועלת"},
    {"word": "נסורת", "meaning": "שאריות עץ, אבקת עץ"},
    {"word": "נפוץ", "meaning": "שכיח, נמצא בכל מקום"},
    {"word": "נפלאות", "meaning": "נפלאות, דברים מופלאים"},
    {"word": "נפח", "meaning": "שיעור התפשטות, מדד כמות"},
    {"word": "נקיטה", "meaning": "פעולה, שימוש במעשה"},
    {"word": "נרגן", "meaning": "מתלונן תמיד, חסר שביעות רצון"},
    {"word": "סבילות", "meaning": "יכולת לשאת, עמידות"},
    {"word": "סגלגל", "meaning": "בצורת ביצה, אליפטי"},
    {"word": "סחף", "meaning": "גרר בעוצמה, שטף"},
    {"word": "סטגנציה", "meaning": "קיפאון, חוסר תנועה"},
    {"word": "סימבולי", "meaning": "סמלי, מייצג"},
    {"word": "סיפור אהבה", "meaning": "רומן, סיפור רומנטי"},
    {"word": "סינרגיה", "meaning": "שיתוף פעולה שהאפקט שלו עולה על סך החלקים"},
    {"word": "סינתזה", "meaning": "חיבור, שילוב"},
    {"word": "ספירה", "meaning": "ספירה, חישוב"},
    {"word": "עיבוי", "meaning": "הפיכת משהו לעבה יותר"},
    {"word": "עיגול", "meaning": "צורה גיאומטרית עגולה"},
    {"word": "עיון", "meaning": "בחינה מדוקדקת, חקירה"},
    {"word": "עידן", "meaning": "תקופה ארוכה, פרק זמן"},
    {"word": "עליזות", "meaning": "שמחה, תחושת אושר"},
    {"word": "עלמה", "meaning": "נערה צעירה, בחורה"},
    {"word": "עמדה", "meaning": "דעה, השקפה"},
    {"word": "ענק", "meaning": "גדול מאוד, עצום"},
    {"word": "עפולה", "meaning": "עיר בצפון ישראל"},
    {"word": "ערמון", "meaning": "סוג של פרי עץ"},
    {"word": "ערער", "meaning": "העלה ספק, פיקפק"},
    {"word": "עשיר", "meaning": "בעל הרבה כסף או משאבים"},
    {"word": "פאזה", "meaning": "שלב, מצב"},
    {"word": "פגע", "meaning": "גרם נזק, היכה"},
    {"word": "פונקציה", "meaning": "תפקיד, פעולה מתמטית"},
    {"word": "פוסט-מודרניזם", "meaning": "תנועה תרבותית שמאתגרת את המודרניזם"},
    {"word": "פורענות", "meaning": "אסון, צרה"},
    {"word": "פזיז", "meaning": "מהיר ובלתי מחושב, נמהר"},
    {"word": "פלטינה", "meaning": "סוג של מתכת יקרה"},
    {"word": "פנים", "meaning": "החלק הקדמי של הראש, מראה חיצוני"},
    {"word": "פנינים", "meaning": "אבני חן שנוצרות בצדפות"},
    {"word": "פסגה", "meaning": "החלק הגבוה ביותר של הר"},
    {"word": "פסול", "meaning": "לא מתאים, לא חוקי"},
    {"word": "פעוט", "meaning": "קטן מאוד, לא חשוב"},
    {"word": "פקע", "meaning": "נשבר, התפוצץ"},
    {"word": "פרדוקס", "meaning": "סתירה פנימית, דבר שנראה בלתי אפשרי"},
    {"word": "פריזמה", "meaning": "גוף גיאומטרי בעל בסיס משולש או מרובע"},
    {"word": "פריקה", "meaning": "הסרת עומס, שחרור"},
    {"word": "פרישות", "meaning": "חיים בנזירות, התרחקות מחברת אנשים"},
    {"word": "פרנסה", "meaning": "מקור הכנסה, עבודה"},
    {"word": "פרצוף", "meaning": "מראה הפנים, חזות"},
    {"word": "פשוט", "meaning": "קל להבנה, לא מורכב"},
    {"word": "פתולוגי", "meaning": "קשור למחלות, חקר המחלות"},
    {"word": "צדדים", "meaning": "חלקים שונים, פאות"},
    {"word": "צהלה", "meaning": "שמחה, קריאת שמחה"},
    {"word": "צווחה", "meaning": "צעקה חזקה, קריאת פחד"},
    {"word": "צילינדר", "meaning": "גליל, מבנה גלילי"},
    {"word": "צלקת", "meaning": "סימן שנותר לאחר פציעה"},
    {"word": "צלף", "meaning": "אדם שיורה במדויק, שיח קטן"},
    {"word": "צנום", "meaning": "רזה מאוד, כחוש"},
    {"word": "צפצוף", "meaning": "צליל חד וקצר"},
    {"word": "צרוד", "meaning": "קול מחוספס, קול שבור"},
    {"word": "צרת", "meaning": "קושי, בעיה"},
    {"word": "קדום", "meaning": "עתיק, ישן מאוד"},
    {"word": "קוהרנטי", "meaning": "בהיר, הגיוני"},
    {"word": "קיטוע", "meaning": "חיתוך חלקים, הפסקות"},
    {"word": "קיים", "meaning": "נמצא, ממשי"},
    {"word": "קירבה", "meaning": "מצב של קרבה, יחסים טובים"},
    {"word": "קלוקל", "meaning": "פגום, לא טוב"},
    {"word": "קלח", "meaning": "תפרחת של צמח, זרם"},
    {"word": "קלסתרון", "meaning": "תיאור מדויק של פנים"},
    {"word": "קללה", "meaning": "השמצה, הבעת רצון לרע"},
    {"word": "קם", "meaning": "התעורר, התייצב"},
    {"word": "קנאי", "meaning": "חשק לאהבתו, רוצה מה שיש לאחרים"},
    {"word": "קנה", "meaning": "צינור, חלק מאקדח או רובה"},
    {"word": "קציר", "meaning": "איסוף התבואה, חיתוך שדות"},
    {"word": "קציצה", "meaning": "מזון טחון בצורת עיגול קטן"},
    {"word": "רועה", "meaning": "אדם שמגדל ומטפל בעדרים"},
    {"word": "רום", "meaning": "גובה, מעלה"},
    {"word": "רחב", "meaning": "גדול בממד הרוחב, מרווח"},
    {"word": "רחצה", "meaning": "ניקוי במים, טבילה"},
    {"word": "ריאלי", "meaning": "מציאותי, מתאים לעובדות"},
    {"word": "ריזיקו", "meaning": "סיכון, אפשרות לנזק"},
    {"word": "רינדור", "meaning": "תהליך יצירת תמונה ממודל תלת-ממדי"},
    {"word": "ריף", "meaning": "מבנה תת-ימי טבעי, שונית"},
    {"word": "ריקוד", "meaning": "תנועה למוזיקה, מחול"},
    {"word": "רמיזה", "meaning": "רמז דק, הבעת דעה בצורה לא ישירה"},
    {"word": "רעש", "meaning": "קולות רמים ולא נעימים, המולה"},
    {"word": "רצועה", "meaning": "פס ארוך וצר, חבל דק"},
    {"word": "שאיפה", "meaning": "רצון להשיג מטרה, שאיבת אוויר"},
    {"word": "שבועה", "meaning": "התחייבות דתית או חוקית, הבטחה חזקה"},
    {"word": "שגור", "meaning": "נפוץ, שכיח"},
    {"word": "שואב", "meaning": "מכשיר או אדם ששואב נוזלים או אוויר"},
    {"word": "שובר", "meaning": "כרטיס עם ערך כספי, שוברים למימוש"},
    {"word": "שידור", "meaning": "העברת תוכן באמצעי תקשורת, שידור רדיו או טלוויזיה"},
    {"word": "שיטפון", "meaning": "הצפת מים, זרם מים חזק"},
    {"word": "שכלתנות", "meaning": "הסתמכות על השכל, רציונליזם"},
    {"word": "שמן", "meaning": "נוזל שומני, בעל אחוזי שומן גבוהים"},
    {"word": "שנאה", "meaning": "רגש עז של דחייה, חוסר חיבה קיצוני"},
    {"word": "שער", "meaning": "פתח כניסה, מדור בעיתון"},
    {"word": "שתל", "meaning": "חלק חי מושתל, נטע"},
    {"word": "שתיקה", "meaning": "חוסר דיבור, אי השמעת קול"},
    {"word": "שקיקה", "meaning": "רצון עז, תשוקה"},
    {"word": "תבוסה", "meaning": "כישלון מוחלט, הפסד"},
    {"word": "תוכנית", "meaning": "תכנון לעתיד, מסלול פעולה"},
    {"word": "תחקיר", "meaning": "בדיקה מעמיקה, חקירה עיתונאית"},
    {"word": "תמהון", "meaning": "הפתעה, השתוממות"},
    {"word": "תשוקה", "meaning": "רצון עז, חשק עז"}
]

additional_words = [
    {"word": "בלום", "meaning": "מלא, עמוס"},
    {"word": "בדיוני", "meaning": "מבוסס על דמיון, לא אמיתי"},
    {"word": "בר קיימא", "meaning": "שניתן לקיימו לאורך זמן"},
    {"word": "גאות ושפל", "meaning": "עליות וירידות, מצבי רוח משתנים"},
    {"word": "דואלי", "meaning": "כפול, בעל שני צדדים"},
    {"word": "דיכוטומיה", "meaning": "חלוקה לשני חלקים מנוגדים"},
    {"word": "הזדמנות", "meaning": "אפשרות, סיכוי"},
    {"word": "הרפתקה", "meaning": "חווייה מרגשת ולא שגרתית"},
    {"word": "השתקפות", "meaning": "דמות שמשתקפת במראה"},
    {"word": "ואקום", "meaning": "חלל ריק"},
    {"word": "וירטואלי", "meaning": "ממוחשב, לא ממשי"},
    {"word": "זווית", "meaning": "מקום מפגש של שני קווים"},
    {"word": "חבוי", "meaning": "מוסתר, לא גלוי"},
    {"word": "חיובי", "meaning": "מביא תועלת, מועיל"},
    {"word": "חסר תקדים", "meaning": "שלא היה כמותו בעבר"},
    {"word": "טכנולוגיה", "meaning": "מערכות וכלים מתקדמים"},
    {"word": "יוזמה", "meaning": "פעולה שנעשית מיוזמת הפרט"},
    {"word": "כושר", "meaning": "יכולת, גופניות טובה"},
    {"word": "לוגיקה", "meaning": "חוקי חשיבה נכונה"},
    {"word": "מאבק", "meaning": "מלחמה, תחרות קשה"},
    {"word": "מאורע", "meaning": "אירוע חשוב"},
    {"word": "מגבלה", "meaning": "הגבלה, מחסום"},
    {"word": "מדעי החברה", "meaning": "תחום לימוד העוסק בחברה האנושית"},
    {"word": "מהפכה", "meaning": "שינוי יסודי ומהותי"},
    {"word": "מורכב", "meaning": "מסובך, מכיל חלקים רבים"},
    {"word": "מחסום", "meaning": "מכשול, קושי"},
    {"word": "מניפסט", "meaning": "הצהרה ציבורית"},
    {"word": "מסורת", "meaning": "מנהגים העוברים מדור לדור"},
    {"word": "מפעל חיים", "meaning": "עבודה מרובה לאורך זמן"},
    {"word": "משמעות", "meaning": "פירוש, תוכן"},
    {"word": "מתודולוגיה", "meaning": "שיטה, דרך פעולה"},
    {"word": "נגזרת", "meaning": "תוצאה משנית"},
    {"word": "נכסי צאן ברזל", "meaning": "דברים בעלי ערך רב"},
    {"word": "נמלט", "meaning": "ברח, יצא ממקום סכנה"},
    {"word": "סימטרי", "meaning": "שיש בו איזון, שוויון"},
    {"word": "סכנה", "meaning": "מצב של איום"},
    {"word": "ספרות", "meaning": "כתיבה יצירתית"},
    {"word": "עוצמה", "meaning": "כוח, חוזק"},
    {"word": "עקרונות", "meaning": "יסודות, כללים מנחים"},
    {"word": "פער", "meaning": "הבדל גדול, רווח"},
    {"word": "פרדיגמה", "meaning": "תבנית חשיבה מקובלת"},
    {"word": "פרקטי", "meaning": "מעשי, ניתן ליישום"},
    {"word": "פרשנות", "meaning": "הסבר, ביאור"},
    {"word": "צוות", "meaning": "קבוצה העובדת יחד"},
    {"word": "צירוף מקרים", "meaning": "אירועים המתרחשים יחד במקרה"},
    {"word": "קונפליקט", "meaning": "עימות, התנגשות"},
    {"word": "קונספט", "meaning": "רעיון, מושג"},
    {"word": "קריירה", "meaning": "מסלול מקצועי"},
    {"word": "שגשוג", "meaning": "פריחה, הצלחה"},
    {"word": "שוויון", "meaning": "העדר הבדלים"},
    {"word": "שכיחות", "meaning": "תדירות, שיעור הופעה"},
    {"word": "שקוף", "meaning": "ברור, ללא הסתרה"},
    {"word": "תודעה", "meaning": "מצב מודעות"},
    {"word": "תופעה", "meaning": "אירוע, מצב"},
    {"word": "תפיסה", "meaning": "הבנה, קליטה"},
    {"word": "תכנון", "meaning": "הכנה מוקדמת"},
    {"word": "תרבות", "meaning": "מנהגים, אורח חיים"}
]

words.extend(additional_words)

# Randomizing the order of words
random.shuffle(words)

# Adding multiple-choice options
for word in words:
    incorrect_meanings = random.sample([w["meaning"] for w in words if w != word], 3)
    options = [word["meaning"]] + incorrect_meanings
    random.shuffle(options)
    word["options"] = options

current_index = 0
mode = "mcq"  # Default mode is multiple-choice questions

def show_word():
    global current_index
    word_label.config(text=words[current_index]["word"])
    meaning_label.config(text="")
    if mode == "mcq":
        for i, option in enumerate(words[current_index]["options"]):
            option_buttons[i].config(text=option)
    else:
        for button in option_buttons:
            button.pack_forget()

def check_answer(selected_option):
    global current_index
    if words[current_index]["options"][selected_option] == words[current_index]["meaning"]:
        current_index = (current_index + 1) % len(words)
        show_word()
    else:
        meaning_label.config(text="לא נכון, נסה שוב.")

def next_word():
    global current_index
    current_index = (current_index + 1) % len(words)
    show_word()

def prev_word():
    global current_index
    current_index = (current_index - 1) % len(words)
    show_word()

def switch_mode(new_mode):
    global mode
    mode = new_mode
    if mode == "mcq":
        for button in option_buttons:
            button.pack(pady=5)
    show_word()

# Creating the main window
root = tk.Tk()
root.title("לימוד מילים פסיכומטריות")

# Mode selection buttons
mode_frame = tk.Frame(root)
mode_frame.pack(pady=10)

mcq_button = tk.Button(mode_frame, text="שאלות אמריקאיות", command=lambda: switch_mode("mcq"))
mcq_button.grid(row=0, column=0, padx=10)

cards_button = tk.Button(mode_frame, text="כרטיסי מילים", command=lambda: switch_mode("cards"))
cards_button.grid(row=0, column=1, padx=10)

word_label = tk.Label(root, text="", font=("Arial", 24))
word_label.pack(pady=20)

meaning_label = tk.Label(root, text="", font=("Arial", 18))
meaning_label.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

option_buttons = []
for i in range(4):
    button = tk.Button(button_frame, text="", command=lambda i=i: check_answer(i))
    button.pack(pady=5)
    option_buttons.append(button)

prev_button = tk.Button(button_frame, text="קודם", command=prev_word)
prev_button.pack(side=tk.LEFT, padx=10)

next_button = tk.Button(button_frame, text="הבא", command=next_word)
next_button.pack(side=tk.RIGHT, padx=10)

show_word()

root.mainloop()