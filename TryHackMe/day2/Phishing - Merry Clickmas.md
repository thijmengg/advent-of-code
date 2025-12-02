# Phishing - Merry Clickmas

Today is about Phising and social engineering. If you are looking at the AoC (Advent of Cyber) page, you see a video on the top. Click that video to get the correct guide through the tasks. In here I'll explain my thought process, and maybe go into the easter eggs.

After starting the server via `./server.py`, we can see a default login page. Meaning we are running some kind of webserver.

So we start our social engineering attack --> Mass Mailer attack. Follow the steps and we get:
```sh
[02/Dec/2025 22:33:01] "GET / HTTP/1.1" 200 -
[2025-12-02 22:33:01] Captured -> username: admin    password: unranked-wisdom-anthem    from: 10.48.168.0
```

So the next step is to test our found credentials on the real login form. Not the self-hosted one. So we head over to: `http://10.48.168.0` and fill out the form. 

Thats weird, the username does not seem to work. Do we have other username-like things we can try?

We have an email: `factory@wareville.thm`. We can treat this as two different usernames:
- `factory@wareville.thm` and
- `factory`

Lets start with just `factory`, and BINGO. We have access to their mailbox. We see our phising email, and can read their emails. Where we can see:
```html
The request: the client has asked us to manufacture 
and ship 1984000 toys to a mix of retail partners and
 charitable distribution centers within the coming 
 couple of weeks. I know \u2014 it\u2019s a big 
 number, but one we can handle if we coordinate across
  production, QC, packing, and logistics without 
  dropping the ball.
```
Meaning we can give answer to the question: "What is the total number of toys expected for delivery?" -> `1984000`

This completes this Room. There were no indications of easter eggs, as well as the server was quite slow at this point. I'll call it a day for today and see you guys tommorow.