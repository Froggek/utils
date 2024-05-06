# utils
A set of scrits and how-to 

## [genealogy](genealogy)
[Family Echo](https://www.familyecho.com/) is a great (free) SaaS tool, whicl allos you to create, display and export genealogy trees (a.k.a. famlily trees). 

It supports various formats: 
- Plain text 
- CSV
- FamilyScript
- [GEDCOM](https://en.wikipedia.org/wiki/GEDCOM)
and is able to generate a pretty standalone HTML page of your whole tree. 

### What for? 

You might be concerned about privacy: _are you willing to upload and store family-related PII (Personally Identifiable Information) in a free online service?_

This tool intends to **locally de-anonymize** a tree you have created online: 
- Create an anonymous family tree on _Family Echo_, only using anonymous pieces of information (such as: acronyms, nicknames, fake birth dates)
- Download this anonymized HTML tree 
- Build a simple (local) CSV mapping, making the relation between the anonymous information, and the real one 
- Run the script
- And, _voilà_!

### How to?
0. Create a free account on [Family Echo](https://www.familyecho.com/)
1. Create your family tree, only using fake data.
2. For each character:
    - Pick a unique key (e.g. his/her initials)
    Two characters must never have the same key. 
    E.g. _Napoléon Bonaparte_ will be identified through his initials, "NB"
    - For each detail about the character, name them in an anonymous way, after the convention: 

| Name in FamilyTree | Name in mapping (CSV file) | Example |
| --- | --- | --- |
| a | b | c |
| d | e | f |

3. Click on "Download", then pick "Read-only HTML page (one file)"
4. Place that file under the [data](genealogy/data) directory. 
Optionally, rename it conveniently (e.g. "source.html")
5. Under the [data](genealogy/data) folder, create a file (e.g. named mapping.csv)
    - Associate to each character's key the various pieces of information you're aware of: name, surname, date of birth, etc.
    - See an example in [mapping-sample.csv](genealogy/data/mapping-sample.csv)
6. Run the script
7. Your updated HTML tree is created: "target.html", under the [data](genealogy/data) directory. 


