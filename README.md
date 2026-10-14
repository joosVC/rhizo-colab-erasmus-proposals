# RHIZO — Erasmus+ projectontwikkeling

Een gezamenlijke bron voor skills die collega's helpen Europese projecten te ontwikkelen. Het startinterview verzamelt de praktijkvraag; de tweede skill bereidt de wetenschappelijke verkenning voor. De uitwerking richt zich voorlopig op KA2.

## Ontwikkelroute voor KA2

| Stap | Resultaat | Status |
| --- | --- | --- |
| Startinterview | Deelbare startnotitie, bekende informatie en open vragen | Skill beschikbaar |
| Wetenschappelijke verkenning | Engelse Elicit-opdracht → door gebruiker uitgevoerd onderzoeksrapport | Promptskill beschikbaar; uitvoering in Elicit |
| Europese beleidsscreening | Relevante behoeften, cijfers, aanbevelingen en prioriteiten | Later uit te werken |
| Keuzegesprek | Gezamenlijk gekozen projectrichting | Met Joos en projecteigenaar |
| Voorlopige Theory of Change | Veranderlogica, voorwaarden en aannames | Later uit te werken |
| PRP-screening | Overlap, aanvullingen en relevante expertise/partners | Na de voorlopige ToC |

Wetenschap en beleid kunnen deels parallel worden verkend. Het startinterview kan ook voor KA1 dienen; KA1-vervolgskills zijn nog niet ontwikkeld.

## Eerste skill: Erasmus+ startinterview

Het [startinterview](.agents/skills/erasmus-startinterview/SKILL.md) begeleidt een docent of klein groepje collega's in het Nederlands. Het gesprek vertrekt vanuit een behoefte, interesse, mogelijke oplossing of inspirerend bestaand project. Richttijd: 15–20 minuten, aanpasbaar aan de beschikbare tijd.

Het resultaat is één deelbare Nederlandstalige startnotitie met:

- het startpunt in één oogopslag;
- kerninzichten en relevante schoolcontext;
- zichtbare aannames en ontbrekende informatie;
- maximaal drie gerichte onderzoeksvragen;
- een gemotiveerd vervolgadvies en uitnodiging aan collega's/directie.

Een volledige Theory of Change, oplossing, partner, callkeuze of budget is nog niet nodig. Deze skill doet geen extern onderzoek en voorspelt geen financiering.

## Tweede skill: wetenschappelijke onderzoeksopdracht voor Elicit

[Elicit onderzoeksopdracht](.agents/skills/erasmus-elicit-brief/SKILL.md) gebruikt de startnotitie en eventuele afgebakende vragen. Ze stelt alleen gerichte vervolgvragen als iets wezenlijks ontbreekt, en levert één zelfstandige Engelse prompt voor Elicit. Het korte gesprek en de overdracht zijn standaard Nederlands.

De opdracht verkent het oplossingslandschap vanuit een probleem, een voorkeursoplossing of een brede behoefte. Ze vraagt zowel naar gevestigde als opkomende aanpakken, relevante aangrenzende onderzoeksvelden, tegenbewijs, toepasbaarheid en onzekerheden. Elicit wordt gevraagd enkele onderbouwde projectrichtingen te vergelijken; de skill kiest die richtingen niet vooraf.

Start bijvoorbeeld met:

> Gebruik $erasmus-elicit-brief. Hieronder staat onze startnotitie. Maak een Engelse prompt voor Elicit, met extra aandacht voor opkomende aanpakken. Mijn gerichte vraag is: welke voorwaarden moeten in onze school aanwezig zijn?

Voeg de startnotitie toe of geef de inhoud mee. Plak de gegenereerde prompt in Elicit en voer het onderzoek daar uit. Bewaar de prompt, uitvoerdatum, het rapport en de referenties. **De promptskill voert geen onderzoek uit en gebruikt geen API-key.** Het teruggekomen Elicit-rapport is het eindpunt van deze onderzoeksstap; interpretatie en projectkeuzes volgen later.

De [prompttemplate](.agents/skills/erasmus-elicit-brief/assets/elicit-prompt-template.en.md), het [onderzoeksprotocol](.agents/skills/erasmus-elicit-brief/references/research-protocol.md) en de [overdracht naar Elicit](.agents/skills/erasmus-elicit-brief/references/elicit-handoff.md) beschrijven de aanpak. [Evaluatiecriteria](evals/erasmus-elicit-brief/rubric.md) en [validatie](evals/erasmus-elicit-brief/validation.md) beschrijven de controles. Een echt Elicit-rapport is nog nodig om te toetsen hoe goed de onderzoeksopdracht daar wordt gevolgd.

## Taalkeuze

De skillinstructies en methodische referenties zijn Engels. De gesprekken met docenten en startnotitie zijn standaard Nederlands; de onderzoeksopdracht voor Elicit is Engels. De latere conceptnota's en extended concept notes worden Engels; die vervolgskills zijn nog niet gebouwd. Expliciete taalkeuzes gaan voor deze defaults.

## Gebruik

Open deze repository in een Codex-omgeving die lokale skills ondersteunt. Beide skills staan onder `.agents/skills/`.

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

Wijzigingen kunnen via een branch en pull request worden besproken. Houd elke skill bij haar fase en gebruik de bijbehorende scenario's in `evals/` voor regressiecontrole. Zet docentfeedback om in instructies of synthetische voorbeelden; houd echte intakeverslagen, leerlinggegevens en credentials buiten deze privérepository met gedeelde skills.

Voer de structurele controle uit met:

```bash
python3 scripts/validate_skills.py
```

De GitHub-workflow voert dezelfde controle uit. De gedragsproeven zijn tekstuele simulaties; praktijkgebruik door docenten, een echte voice-client en naleving van de Elicit-opdracht door Elicit moeten nog worden getoetst. Zie de validatienotities per skill in `evals/`.

Documentatie voor het skillformaat: [OpenAI — Build skills](https://learn.chatgpt.com/docs/build-skills).
