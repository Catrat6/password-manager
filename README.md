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







