import os
import time
from colorama import Fore, Style, init

# تهيئة colorama لتنسيق الألوان
init(autoreset=True)

# واجهة المستخدم
def show_interface():
    print(Fore.GREEN + Style.BRIGHT + '''
    *******************************************************
    *             Spam-SMS Tool                          *
    *         Developed by: Dev Cherki                   *
    *                                                     *
    *   Contact Me:                                      *
    *   Facebook: https://www.facebook.com/dev.cherki     *
    *   Instagram: https://www.instagram.com/dev_cherki   *
    *******************************************************
    ''')

# إرسال الرسائل النصية عبر Termux API
def send_sms():
    # تحديد مسار ملف الأرقام
    file_path = "/sdcard/Download/data.txt"

    try:
        # قراءة الأرقام من الملف
        with open(file_path, "r") as file:
            numbers = file.readlines()

        # إرسال الرسائل النصية باستخدام Termux API
        for number in numbers:
            number = number.strip()  # إزالة المسافات البيضاء
            if number:  # التأكد من أن الرقم غير فارغ
                # تضمين اسم الأداة في بداية الرسالة
                message = "Spam-SMS Tool: مرحبًا، هذه رسالة تجريبية مرسلة من Python عبر Termux API."
                os.system(f'termux-sms-send -n {number} "{message}"')
                print(Fore.YELLOW + f"تم إرسال الرسالة إلى: {number}")
                time.sleep(1)  # تأخير بسيط بين الرسائل لإعطاء الوقت

    except FileNotFoundError:
        print(Fore.RED + f"لم يتم العثور على الملف: {file_path}")
    except Exception as e:
        print(Fore.RED + f"حدث خطأ: {str(e)}")

# عرض واجهة المستخدم وبدء إرسال الرسائل
def main():
    show_interface()  # عرض الواجهة
    send_sms()        # بدء إرسال الرسائل

# تنفيذ السكربت
if __name__ == "__main__":
    main()
