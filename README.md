# RHIZO — Erasmus+ projectontwikkeling

Een gezamenlijke bron voor skills die collega's helpen Europese samenwerkingsprojecten te ontwikkelen. De eerste skill verzamelt het startverhaal en maakt duidelijk wat de volgende stap is.

## Eerste skill: Erasmus+ startinterview

Het [startinterview](.agents/skills/erasmus-startinterview/SKILL.md) begeleidt een docent of klein groepje collega's in het Nederlands. Het gesprek vertrekt vanuit een behoefte, interesse, mogelijke oplossing of inspirerend bestaand project. Richttijd: 15–20 minuten, aanpasbaar aan de beschikbare tijd.

Het resultaat is één deelbare Nederlandstalige startnotitie met:

- het startpunt in één oogopslag;
- kerninzichten en relevante schoolcontext;
- zichtbare aannames en ontbrekende informatie;
- maximaal drie gerichte onderzoeksvragen;
- een gemotiveerd vervolgadvies en uitnodiging aan collega's/directie.

Een volledige Theory of Change, oplossing, partner, callkeuze of budget is nog niet nodig. Deze skill doet geen extern onderzoek en voorspelt geen financiering.

## Taalkeuze

De skillinstructies en methodische referenties zijn in het Engels geschreven. De voorbeeldvragen, welkomsttekst en rapporttemplate zijn Nederlands. Ook de daadwerkelijke uitvoering en startnotitie zijn standaard Nederlands. De latere conceptnota's en extended concept notes worden Engels; die vervolgskills zijn nog niet gebouwd.

## Gebruik

Open deze repository in een Codex-omgeving die lokale skills ondersteunt. De skill staat op de gedocumenteerde locatie `.agents/skills/erasmus-startinterview/`.

Start bijvoorbeeld met:

> Gebruik $erasmus-startinterview. Ik wil een eerste idee voor een Europees samenwerkingsproject verkennen. Ik heb ongeveer vijftien minuten.

Spreek of dicteer antwoorden als jouw omgeving dat ondersteunt. Typen kan ook. De skill activeert geen microfoon en bevat geen eigen spraaksoftware.

**Publicatie in GitHub installeert de skill niet automatisch in ChatGPT.** Voor gebruik door collega's buiten een repositoryomgeving is installatie of distributie via een ondersteunde skill/plugin-omgeving een aparte stap. Voor een handmatige proef kan een omgeving die bestanden kan lezen de skillmap met alle referenties en assets krijgen; vraag expliciet de SKILL.md en de daarin vereiste bestanden te volgen. Dit is geen garantie dat iedere voice-client lokale skills laadt.

## Inhoud

| Bestand | Functie |
| --- | --- |
| [SKILL.md](.agents/skills/erasmus-startinterview/SKILL.md) | Trigger, grenzen, workflow, taal en output |
| [Interviewprotocol](.agents/skills/erasmus-startinterview/references/interview-protocol.md) | Dynamisch gesprek, tijdsturing en afronding |
| [Vraagbank](.agents/skills/erasmus-startinterview/references/question-bank.nl.md) | Nederlandstalige vervolgvragen per vertrekpunt |
| [Bewijs en vervolgstappen](.agents/skills/erasmus-startinterview/references/evidence-and-next-steps.md) | Ervaringen, vermoedens, open vragen en routeadvies |
| [Rapporttemplate](.agents/skills/erasmus-startinterview/assets/startnotitie-template.nl.md) | Deelbare kernpagina en optionele context |
| [Methodische bronnen](.agents/skills/erasmus-startinterview/references/method-sources.md) | Onderbouwing en afbakening van de aanpak |
| [Evaluatiecriteria](evals/erasmus-startinterview/rubric.md) | Gedrag en output waarmee we de skill toetsen |

## Samen verbeteren

Wijzigingen kunnen via een branch en pull request worden besproken. Houd de interviewskill afgebakend en gebruik de scenario's in `evals/erasmus-startinterview/` voor regressiecontrole. Zet concrete docentfeedback om in verbeteringen van instructies of voorbeelden; voeg geen echte intakeverslagen of leerlinggegevens toe aan deze openbare repo.

Voer de structurele controle uit met:

```bash
python3 scripts/validate_skills.py
```

De GitHub-workflow voert dezelfde controle uit. De gedragsproeven in [de validatienotitie](evals/erasmus-startinterview/validation.md) zijn tekstuele simulaties; praktijkgebruik door docenten en de ervaring in een echte voice-client moeten nog worden getoetst.

Documentatie voor het skillformaat: [OpenAI — Build skills](https://learn.chatgpt.com/docs/build-skills).
