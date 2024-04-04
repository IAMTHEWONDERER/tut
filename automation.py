import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

from dotenv import load_dotenv

PORT = 587  
EMAIL_SERVER = "smtp-mail.outlook.com"  
#loading everything
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir /".env"
load_dotenv(envars)
print("working in port")

#environment variables
sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")


def send_email(subject, receiver_email, name, attachments):
    msg = EmailMessage()
    msg["subject"] = subject
    msg["from"] = formataddr(("Oussama ALOUCHE", f"{sender_email}"))
    msg.set_content(
        f"""\
      Madame, Monsieur,
Je me permets de vous adresser ce courrier afin de vous exprimer mon intérêt pour d'éventuelles opportunités au sein de votre entreprise dans le domaine du développement web. Ayant récemment pris connaissance de votre entreprise, j'ai été impressionné par votre réputation et votre engagement envers l'innovation.

Actuellement à la recherche d'un stage ou d'un poste junior en développement web, je suis titulaire d'une Licence Fondamentale en Sciences des Matières Physique Chimie obtenue à la Faculté des Sciences de Rabat. Au cours de ma formation et de mes expériences professionnelles, j'ai acquis une solide expertise dans le développement web, notamment avec la pile MERN (MongoDB, ExpressJS, NodeJS, React), ainsi qu'en langages Javascript, HTML, CSS et Typescript.

Mes compétences comprennent également le design UI/UX, la gestion de projet et la rédaction de rapports. Je suis passionné par la technologie et je suis convaincu que mon profil pourrait correspondre aux besoins de votre entreprise.

Je vous serais reconnaissant de bien vouloir me tenir informé de toute opportunité de stage ou de poste junior disponible au sein de votre entreprise. Je reste à votre disposition pour toute information complémentaire et je suis disponible pour un entretien à votre convenance.

Je vous remercie de l'attention que vous porterez à ma candidature et je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées.

Cordialement,

Oussama ALOUCHE



Numéro de téléphone : 06 93 81 04 38
Adresse email secondaire : theoblivionitself@gmail.com
"""
    )
    #added email that will be sent as html code 
    print("working in adding email ")
    msg.add_alternative(
        f"""\
            <html>
            <body>
                <h1> Madame, Monsieur,</h1>
            
            <p> Je me permets de vous adresser ce courrier afin de vous exprimer mon intérêt pour d'éventuelles opportunités au sein de votre entreprise dans le domaine du développement web. 
            Ayant récemment pris connaissance de votre entreprise, j'ai été impressionné par votre réputation et votre engagement envers l'innovation.
            <br/>
            Actuellement à la recherche d'un stage ou d'un poste junior en développement web, je suis titulaire d'une Licence Fondamentale en Sciences des Matières Physique Chimie obtenue à la Faculté des Sciences de Rabat.
            Au cours de ma formation et de mes expériences professionnelles, j'ai acquis une solide expertise dans le développement web, notamment avec la pile MERN (MongoDB, ExpressJS, NodeJS, React), ainsi qu'en langages Javascript, HTML, CSS et Typescript.

            <br/>
            Mes compétences comprennent également le design UI/UX, la gestion de projet et la rédaction de rapports. Je suis passionné par la technologie et je suis convaincu que mon profil pourrait correspondre aux besoins de votre entreprise.
            <br/>

            Je vous serais reconnaissant de bien vouloir me tenir informé de toute opportunité de stage ou de poste junior disponible au sein de votre entreprise. Je reste à votre disposition pour toute information complémentaire et je suis disponible pour un entretien à votre convenance.
            Je vous remercie de l'attention que vous porterez à ma candidature et je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées.
       </p>
<br/>

<p>Cordialement, <br/>

Oussama ALOUCHE</p>

<p> Numéro de Télephone : 06 93 81 04 38 </p>
<p>Adresse Email :theoblivionitself@gmail.com <br/>

mes CV en français est anglais: 
<a href='portfolioENG.pdf'> English Resume, </a> <br/> <a href='portfolioFR.pdf'> Resumé en français. </a>
</p>
            """,
            subtype="html",
    )
    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        
if __name__ == '__main__':
     send_email(
         
         subject=" Demande de stage ou de poste junior en développement web fullstack, backend ou frontend.",
         name="Recruiteur",
         receiver_email="oussama6710@gmail.com",
         attachments="<a href='portfolioENG.pdf'> English Resume, </a> <br/> <a href='portfolioFR.pdf'> Resumé en français. </a>",
         
     )
     
     print("everything should work")