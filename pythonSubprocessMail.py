import subprocess


def send_mail(body, sub, file_name):
    mailbody = subprocess.Popen(['echo', body], stdout=subprocess.PIPE)
    if (file_name != "no"):
        sendmail = subprocess.Popen(['mailx', '-s', sub, '-a', file_name, 'g.bhargav007@yahoo.com'],
                                    stdin=mailbody.stdout, stdout=subprocess.PIPE)
    else:
        sendmail = subprocess.Popen(['mailx', '-s', sub, 'g.bhargav007@yahoo.com'], stdin=mailbody.stdout,
                                    stdout=subprocess.PIPE)
    end_of_pipe = sendmail.stdout


send_mail("ok .... We are Getting mail using unix commnads ", "Testing Email Uinx Functionality", "no")