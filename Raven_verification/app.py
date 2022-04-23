# -*- coding: utf-8 -*-

# Hi there Bruv !
# This site was created by RUET::CSE-20("Mehedi Hasan")


# How it works ?

# 1. User will put roll number and his/her Telegram ID.
# 2. Backend Cypher will check if the roll number is valid or not
# 3. If valid, site will show a link to the user
# 4. If not valid, then you'll see "Itachi Uchiha" or "Boruto Uzumaki"  (0.*)

# (FOR DEV) "Backup section" is for typical backup of the database into your git repo




# Guideline for Dumb MeEk_0
# use on terminal    :  export FLASK_APP=app.py
# then do :  flask run or flask run --port=2000 to start listening to port 2000
# or use "gunicorn" : commands are "gunicorn app:app"


import time
import os
import sqlite3
from flask import *
from flask import Flask, render_template
app = Flask(__name__)



# Backup section


# Demo :
# remote_repo_URL= "www.github.com/YORU/rifter_will_handel_this.git"

save = """
remote_repo_URL="${{REPLACE_WITH_GIT_DB_URL}}"
git config --global user.name "${{GIT_USER_NAME}}"
git config --global user.email "${{GIT_USER_EMAIL}}"
cd db
rm -rdf .git
git init
git add .
git commit -m "initial commit"
git remote add origin $remote_repo_URL
git push
git remote -v
git push --force origin master
"""




# main page to show !

server = """
<html>
<head>
    <link href="https://fonts.cdnfonts.com/css/valorant" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Ubuntu:ital,wght@1,500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <style>
        #copy {
            border: 0px;
            font-family: Ubuntu;
            color: blue;
            font-size: 18px;
            background: #fff;
        }

        span {
            color: #fa4454;
            font-family: 'Ubuntu', sans-serif;
        }

        #meek {
            font-family: VALORANT;
            font-size: 12px;
            bottom: 0px;
            margin-left: 42%;
            margin-bottom: 5%;
            align-items: center;
            position: fixed;
        }

        #mlink {
            color: #fa4454;
            text-decoration: none;
        }
    </style>
    <title>
        Verification By Raven !
    </title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>

<body>
    <div class="container">
        </br>
        <label for="roll"><span class="notice">Remember to set your Telegram Privacy Policy > Who Can add you to group> to "Anybody" in your telegram setting </br>Otherwise, The link will not work for you !</span><p>Telegram Id  ( Get it from <a href="https://t.me/myidbot">here</a>. Click to copy <button id="Copy" value="">/getid</button> and send it to the bot then paste the number bellow) <a href="https://telegra.ph/Guide-Follow-Me-12-20" target="_balnk"> Visual Guide</a></p></label>
        <form method="POST" name="myForm">
            <div class="form-group">
                <input type="number" class="form-control" id="id" name="id" placeholder="Enter Your Telegram Id no "></br>
                <label for="roll">RKCuet Roll</label>
                <input type="number" class="form-control" id="roll" name="roll" placeholder="Enter Roll to verify your Identity ">
                <small class="form-text text-muted">Enter Your Own Roll !</small>
            </div>
            <button type="submit" class="btn btn-primary" id="submit">Submit</button>
        </form>
    </div>
    <div>
        <p id="meek">
            <a href="https://t.me/MeEk_0" id="mlink">©MeEk_0</a>
        </p>
    </div>
</body>
<script>
    function Clipboard_CopyTo(value) {
        var tempInput = document.createElement("input");
        tempInput.value = value;
        document.body.appendChild(tempInput);
        tempInput.select();
        document.execCommand("copy");
        document.body.removeChild(tempInput);
    }

    document.querySelector('#Copy').onclick = function() {
        Clipboard_CopyTo('/getid');
    }


    document.getElementById("submit").onclick = function() {
        var roll = document.getElementById("roll")
        var id = document.getElementById("id")

        if ((id.value.length === 0) && (roll.value.length === 0)) {
            alert("Fill All the Fields");
            id.style.borderColor = 'Red';
            roll.style.borderColor = 'Red';
            return false;
        } else if ((id.value.length === 0) && (roll.value.length != 0)) {
            alert("Fill Your Telegram id");
            roll.style.borderColor = 'initial';
            id.style.borderColor = 'Red';
            return false;
        } else if (roll.value.length === 0 && id.value.length != 0) {
            alert("Fill Your RKCuet Roll");
            id.style.borderColor = 'initial';
            roll.style.borderColor = 'Red';
            return false;
        } else {
            id.style.borderColor = 'initial';
            roll.style.borderColor = 'initial';
            return true;
        }
    }
</script>
</html>
"""




# For imposters ! Itachi Is here !

impostor = """
<html>

<head>
    <title>Raven Detected Imposter</title>

    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
</head>

<body onload="">
    <link href="https://fonts.cdnfonts.com/css/valorant" rel="stylesheet">
    <style>
        *,
        *:before,
        *:after {
            margin: 0px;
            padding: 0px;
            box-sizing: border-box;
        }

        body {
            min-width: 1300px;
            width: 100%;
            height: 200vh;
            background: #010506;
            overflow: hidden;
        }

        .itachi {
            background-image: url(https://i.ibb.co/nmZcjBJ/itachi-finger.jpg);
            background-size: contain;
            background-repeat: no-repeat;
            position: absolute;
            min-width: 1300px;
            background-attachment: fixed;
            width: 100%;
            height: 200vh;
            border: 0px;
        }

        .itachiText {
            font-family: VALORANT;
            color: #fa4454;
            padding: 91px;
            font-size: 50px;
            position: fixed;
        }
        /* Small screens */

        @media only screen and (max-width: 600px) {
            body {
                min-width: 400px;
                width: 100%;
                height: 700px;
                background: #0000;
            }
            .itachi {
                background-color: #ffff;
                background-image: url(https://i.ibb.co/TWR3jvP/cocky.jpg);
                background-size: contain;
                background-repeat: no-repeat;
                position: fixed;
                width: 100%;
                height: 100vh;
                border: none;
            }
            .itachiText {
                font-family: VALORANT;
                color: #fa4454;
                padding: 20px;
                font-size: 25px;
                position: relative;
            }
        }
    </style>
    <audio loop id="audio"></audio>
    <!-- audio will be changed by js. Check the down section  -->
    <div class="container">
        <img class="itachi">
        <p class="itachiText">You Impostor !</p>
    </div>
</body>
<script>
    const source_main = ['https://media1.vocaroo.com/mp3/1mhwo3faZiVs', 'https://media1.vocaroo.com/mp3/14q8hA75xMob']

    if (window.screen.width * window.devicePixelRatio <= 1100) {
        source = source_main[1];
    } else {
        source = source_main[0];
    }
    var audio = document.getElementById("audio");
    //
    audio.autoplay = true;
    //
    audio.load()
    audio.addEventListener("load", function() {
        audio.play();
    }, true);
    audio.src = source;

    var loopCount = 0;
    document.getElementById("audio").addEventListener("timeupdate", function() {
        if (this.currentTime == 0) {
            ++loopCount;
            if ((loopCount == 3) && (window.screen.width * window.devicePixelRatio <= 1100)) {
                audio.pause();
            } else if ((loopCount == 5) && (window.screen.width * window.devicePixelRatio >= 1100)) { // to set different audio on small screens
                audio.pause();
            }
        }
    });
</script>
</head>

</html>
"""




# If found In DB
link = """
<html>
<title>
    Found !
</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Ubuntu:ital,wght@1,500&display=swap" rel="stylesheet">
<link href="https://fonts.cdnfonts.com/css/valorant" rel="stylesheet">
<style>
   body {
       background: white;
       color: black;
   }
    #name {
        font-size: 100%;
        font-family: VALORANT;
        color: #fa4454;
    }
    #link{
        color: #fa4454;
        text-decoration: none;
    }

    .contact {


        text-align: center;
        font-size: 200%;
        font-family: Ubuntu;
    }
      @media only screen and (max-width: 600px) {
        #name {
            font-size: 70%;
            }
        .contact {
            margin-top: 30%;
            font-size: 100%;
            }
        #link{
            font-size: 70%;
            font-family: Ubuntu;
            color: #fa4454;
            }
        }
</style>

<body>
    <div class="contact">
        <p>Found You 🤘</p>
        <p>
            <h2>Hello <span id="name">{{name}}</span></h2>
        </p>
        <p>
            <h3>Your link to join is : <a id="link" href={{invite}}> <u>Here ! </u></a></h3>
        </p>
    </div>
    <div class="img">
        <img id="logo">
    </div>

</body>

</html>
"""



# Works As a MiddleMan  IN our verification if roll wasn't found

middleManResult = """
<html>
<title>
    Roll Not Found !
</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Ubuntu:ital,wght@1,500&display=swap" rel="stylesheet">
<link href="https://fonts.cdnfonts.com/css/valorant" rel="stylesheet">
<style>
   body {
       background: white;
       color: black;
   }
   #meek {
            font-family: Ubuntu;
            font-size: 12px;
            bottom: 0px;
            margin-left: 42%;
            margin-bottom: 5%;
            align-items: center;
            position: fixed;
        }
    #mlink {
        font-family: VALORANT;
        color: #fa4454;
        text-decoration: none;
        }
    #name {
        font-size: 100%;
        font-family: VALORANT;
        color: #fa4454;
    }
    #link{
        color: #fa4454;
        text-decoration: none;
    }

    .contact {
        /* margin-top: 50vh; */
        text-align: center;
        font-size: 200%;
        font-family: Ubuntu;
    }

    #by{
        font-size: 100%;
        font-family: Ubuntu;
        color: #fa4454;
    }
    @media only screen and (max-width: 600px) {
        #name {
            font-size: 70%;
            }
        .contact {
            margin-top: 30%;
            font-size: 100%;
            }
        #by{
            font-size: 70%;
            font-family: Ubuntu;
            color: #fa4454;
            }
        }
</style>

<body>
    <div class="contact">
        <p>Roll Wasn't Found !</p>
        <p>
            <h2>Hey <span id="name">{{name}}</span></h2>
        </p>
        <p>
            <h3>Your Roll was Entered By : <span id="by">{{by}}</span></h3>
        </p>
    </div>
    <div>
        <p id="meek">Complain to <a href="https://t.me/MeEk_0" id="mlink"> MeEk_0</a></p>
    </div>

</body>
</html>
"""




def verify(input):
    user_input =[]
    user_input.append(input[0])
    user_input.append(input[1])
    print(f"user input {input}")
    conn = sqlite3.connect("db/ruetians-1.db")
    c = conn.cursor()
    c.execute("SELECT name,links FROM ruetians WHERE roll=?", (user_input[0],))
    output = (c.fetchone())
    print(f"result{output}")
    if output is not None:
        msg = render_template_string(link, name=output[0], invite = output[1])    #if any error occurs DB will be safe by this way
        c.execute("UPDATE ruetians SET by=:by WHERE roll=:roll",
                  {'by': user_input[1], 'roll': user_input[0]})
        c.execute("UPDATE ruetians SET roll=0 WHERE roll=?", (user_input[0],))
        conn.commit()
    else:
        msg = None
    return msg


@app.route('/', methods=['POST'])
def get_var():
    inputs = []
    inputs.append(request.form['roll'])
    inputs.append(request.form['id'])
    final = verify(inputs)
    if final is not None:
        os.system(save)
        return final
    else:
        conn = sqlite3.connect("db/ruetians-1.db")
        c = conn.cursor()
        c.execute("SELECT name,by FROM ruetians WHERE backup=?", (inputs[0],))
        output = (c.fetchone())
        if output is not None:
            return render_template_string(middleManResult, name= output[0], by= output[1])
        else:
            return impostor


@app.route("/")
def home():
    return server



if __name__ == "__main__":
    app.run(debug=True)
