```commandline

            .-""-.
           / .--. \
          / /    \ \
          | |    | |
          | |.-""-.|
         ///`.::::.`\
        ||| ::/  \:: ;
        ||; ::\__/:: ;
         \\\ '::::' /
          `=':-..-'`
```
## Update 5/7/2024

Ok so for the most part everything works completely as I intended at this point. I started some basic tasks
on my laptop, messed something up and then got carried away. Anyway it is now completely useable and all features
work.

- Password Generator Displays as a pop up in a second window. You can generate both random string passwords or 
  random phrases and pick the length as well.
        - This still need to be smoothed out, also I realized at the end of the sprint that normal messageboxes
            in tkinter can not be copied and pasted or really modified so next I will be fixing that and making
          a full on window for it.
- Ecryption state persists between application runs and all the features that would require it work. You can leave
  it encrypted when your not using it and un encrypt when you are with the click of a button. 
        - This also needs perfection, as of right now obviously anyone can just click the button and decrypt 
            you data, i will leave this like this for testing simplicity until I package it. When I am ready
            and in the end phase I will make it so you must import you key to unlock it and the key will 
            NOT be stored on the application in the end product.
- Everything else works great.

Mostly its all visual type stuff left, I am sure its also a mess on mac and other platforms because I have only
really ran it on my PC.

### Whats next?

- Build a prettier pop up window to use for all the pop up windows.
- smooth out the apperance and make a mini theme option.
- Go back over the code and minimize and test
- Finalize the encryption so that the key is input to unlock it instead of being stored in the app, or I may make
  it an option as I am sure some people would be happy with how it is.
- Package it.



## Password Manager

Ok kinda went nuts on this and put way too much time in the wrong direction.
At first I wanted to to only encrypt the passwords in the CSV but had 
a hell of a time getting the fernet and pandas to work together, Maybe there
is a way but I did not find it and I went through a TON of trouble shooting
via Stack Overflow and Chat GPT. I will admit encryption is not my strong suit
though so it easily could be something dumb and stupid I was doing wrong.

## Better Idea Through Failure

Its all ok though because a better idea resulted from my failure. Why encrypt just
the password when I can just encrypt and un encrypt the whole file pretty easily.

## As it exists now

We are getting pretty close. The app is completely functional, writing to the CSV 
works great and you can encypt and un encrypt the data with the click of a button.

- Website, Username, Password stored in a CSV.
- You can recall the password by typing in the name of the website, this means
  you never have to read the CSV, so it is now fully functional.
- A button also allows you to run encryption on the file to lock it and then 
  unlock it again by re-clicking the button.

## So whats Wrong?

Nothing that cant be solved but I am tired for now so I will work more on this later.

- Right now even though the encryption is obviously permanent the state of the 
 file does not persist between program runs so any feature like detecting if the file
 is encrypted before trying to write or read and encryption itself break if it is restarted
 not exactly a hard fix but I just need a break from this before I continue.

Also the biggest issue with this is that if you restart the program after encryption
you CAN NOT unencrypt, clicking the button encrypts the encryption basically breaking
the entire program for any would be end user lol.

Anyways again, easy fix.

## Next Steps

So on my next session with this application here is what I will be building:

- A function that saves encryption state to an external .txt to maintain the state
  between runs.
- Right now there is a generate password button, not that its complicated I had just
  set it on the back burner while I was writing everything else.
- Perfection of pop up windows.
- Lastly the encryption button will go from just a button to a field and a button
  that will require the key to unlock it once encrypted. I will also provide
  a toggle switch to turn this off so the user can choose if the key will be 
  required to unlock it or not.
- Lastly I will add themes and maybe an easy to toggle menu for themes.







