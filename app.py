from flask import Flask,render_template,url_for,request
import  smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import datetime

app = Flask(__name__)


def enviarMSG(nome,docfn,curso,respo_exame):






    data = datetime.datetime.now()

    data = str(data).split(".")[0]

    todamsg = "nome: "+ nome+"\nData de Realizacao: "+data+"\nCurso: "+curso+"\nrespostas: "+respo_exame


    msg = MIMEMultipart()
    msg["Subject"] = "Exame de: "+ nome
    msg["From"] = "mozlimoz0rc@gmail.com"
    msg["To"] = "scaybuch@gmail.com"
    password = "vqcmikhtvwmvooab"
    #msg.add_header("Content-Type", "text/html")
    msg.attach(MIMEText(todamsg,"html"))

    #adicionando o documento


    argv = open("static/docsb/"+docfn,"rb")

    argv_data = argv.read()
    argv_name = argv.name

    att = MIMEBase('application','octet-stream')
    att.set_payload(argv_data)
    encoders.encode_base64(att)

    att.add_header('Content-Disposition', f"attachment; filename= {argv_name}")
    

    msg.attach(att)











    #msg.add_attachment(argv_data,maintype="application", subtype="octet-stream", filename= argv_name)



    #enviando o credecial
    s = smtplib.SMTP('smtp.gmail.com: 587')
    #login de credenciai
    s.ehlo()
    s.starttls()
    s.login(msg["From"],password)
    s.sendmail(msg["From"],[msg["To"]],msg.as_string())
    s.quit()

    return "Inscricao Feita Com Sucesso!"






@app.route("/",methods=["GET","POST"])
def exame():
    nome = ""
    data = ""
    docf = None
    docname= None
    certifname= None


    if request.method == "POST":
        nome = request.form["nome_completo"]
        respo = request.form["Respostas_Exame"]
        curso = request.form["curso_"]

        #    return render_template("inscricao.html",titulof = "Carrega o Documento e o Certificado! para poder fazer Inscricaio.")
        
        docf = request.files["documento_foto"]

        docname = docf.filename

        if docname == "":
            return render_template("index.html",errorS = "o arquivo do documento esta corrompido! ")

        #crie uma coisa para checar a instecao


        docf.save(os.path.join("/static/docsb",docname))
        
        try:
            print("nome:", nome)
            print("doc", str(docname))
            try:
                respo= enviarMSG(nome,docname,curso,respo_exame)
            except Exception as e:
                respo = "Erro ao Submeter "+str(e)+""
                print(respo)

            return render_template("exameSucess.html",aluno = respo)

        except Exception as e2:
            print("error")
            return render_template("index.html",errorS = "Err "+str(e2) )
            print(e2)






        
    else:
        print("formulario InValido")
        
    return render_template("index.html",errorS= "Responda Adequadamente o Exame." )




if __name__ == "__main__":
    app.run(debug="True")


