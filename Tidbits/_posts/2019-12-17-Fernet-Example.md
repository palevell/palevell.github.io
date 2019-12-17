---
layout:     post
title:      Fernet Encryption Example
date:       2019-12-17 6:12:17 -0500
modified:   2019-12-17 6:12:17 -0500
version:    0
categories: Tidbits
tags:       [ gist, infosec, cryptography, encryption, fernet, examples ]
excerpt:    This is the best (useful) example of Fernet encryption that I have 
            found, so far.
slug:       fernet-encryption-example
---

After being less than satified with the results of my efforts to incorporate 
encryption into one of my Flask projects with existing Flask modules, I started 
researching what is generally available for Python, [here][search1] and 
[here][search2], which led me to the [cryptography][crypto] package.

From the project description:
> cryptography is a package which provides cryptographic recipes and primitives 
> to Python developers.  Our goal is for it to be your “cryptographic standard 
> library”. 

Upon browsing the code snippets, I noted that this library references 
**"Fernet"**.  Data encryption is something I understand at a high level, 
but not something that I have implemented in a project, until now.  One 
reason that I have been slow to get into web application development is 
that there aren't enough people doing #InfoSec **well**.  It seems like 
every week there is a massive new data breach of systems that should be 
hardened against such attacks.

### What is Fernet?

In simple terms, [Fernet][fernet] is the encryption methodology used by 
[Python's][python] [cryptography][crypto] package.  The Fernet specification 
can be found [here][spec].

### How is Fernet used?

Fernet can be used to securely store sensitive information, like credit card 
numbers, access tokens, etc.  Storing these is different that how most passwords 
are stored.  These days, it is common to store only the [hash][hashdef] of a 
password, and not the password, itself.

There is no way to recover a password from its hash.  This is method is useless for 
storing information that we actually want to read, later.

#### Example

{% gist bb034b559bb9dde9911c97219b6889ad %}


### Observations

In many circles, poor data security is a cardinal sin.  The very notion of adding 
security AFTER an IT project is built is tantamount to pouring a foundation AFTER 
the house is built--it simply doens't make sense.  It is always easier to build 
security into a project, rather than retro-fit it.  These big companies that 
experience data breaches need to seriously reconsider how their software is 
designed.  The sad part is that an entire industry has evolved out of poor data 
security, and many organizations are simply unwilling to spend the money to 
properly secure their data.

### Summary

Python's [cryptography][crypto] package and [Fernet][fernet] are one of the 
easiet ways to secure your application's secrets.  Learning to use it and 
getting good at it could keep you from being mentioned in the next breaking 
news story about a big data breach.

&nbsp;

----------

&nbsp;

### References

[Abdou Rockikz][abdou], [*How to Encrypt and Decrypt Files in Python*][ref1], September 29th, 2019

[abdou]:    https://www.thepythoncode.com/author/1
[crypto]:   https://cryptography.io/en/latest
[fernet]:   https://cryptography.io/en/latest/fernet
[flask]:    https://palletsprojects.com/p/flask
[hashdef]:  https://en.wikipedia.org/wiki/Cryptographic_hash_function
[infosec]:  https://twitter.com/hashtag/infosec
[python]:   https://python.org
[ref1]:     https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
[search1]:  https://pypi.org/search/?q=encryption
[search2]:  https://pypi.org/search/?q=cryptography
[spec]:     https://github.com/fernet/spec



