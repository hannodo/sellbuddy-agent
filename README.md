# SellBuddy

Ein teilbarer, deutschsprachiger Skill für private Verkäufe: Anzeigen aus Fotos
erstellen, Anfragen beantworten, Abholungen koordinieren und Preise nach vereinbarten
Regeln prüfen. Mit geführtem Einrichtungsinterview statt versteckter Standardvollmachten.

Es enthält keine persönlichen Verkaufsdaten, Fotos, Käuferkontakte oder Zugangsdaten.
Kein offizielles Produkt eines Plattformbetreibers, von OpenAI oder von Anthropic.

## Zuerst die Plattformregeln prüfen

SellBuddy ist eine plattformneutrale Arbeitsanleitung, keine Freigabe zur
Automatisierung einer bestimmten Website. Manche Verkaufsplattformen beschränken
automatisierte Zugriffe oder das Sammeln von Inhalten und verlangen eine ausdrückliche
Zustimmung. Ein lokaler Browser und ein eigener Account ändern diese Regeln nicht.
Ein neutraler Projektname ist ebenfalls kein Schutz vor einem Regelverstoß.

Vor Browserzugriff und regelmäßigen Checks die aktuellen Bedingungen der gewählten
Plattform prüfen und erforderliche Erlaubnisse einholen. Unklare oder nicht erlaubte
Automatisierung nicht starten. Stattdessen kann SellBuddy aus deinen hier bereitgestellten
Fotos und Angaben Texte, Antwortentwürfe und eine lokale Verkaufsübersicht erstellen;
du bedienst die Plattform dann selbst. Keine rechtliche Beratung oder Zusicherung
einer Plattformkompatibilität.

## Was du brauchst

Für den Browsermodus brauchst du einen Account auf der gewählten Verkaufsplattform,
deren Erlaubnis für die gewünschte Nutzung, einen lokalen Browser und einen Agenten, der diesen
Browser tatsächlich bedienen kann. Empfohlene Wege:

- Codex-/ChatGPT-Desktop-App mit lokalem Browserzugriff.
- Claude Code mit Claude-in-Chrome-Anbindung; CLI oder geeignete lokale Desktop-Code-Umgebung.

Die normalen Chatfenster ohne Browserwerkzeuge reichen nicht. Ein Cloud-Browser
ist kein verlässlicher Ersatz für dein lokales eingeloggtes Profil. Dass jeder
Cloud-Browser generell gesperrt wird, wird hier nicht behauptet.
Claude Desktop ist für den dokumentierten Claude-Code-CLI-Weg nicht erforderlich.
Funktionsverfügbarkeit kann von Tarif, Betriebssystem, App-Version und Organisation abhängen.

## In vier Schritten starten

1. Über **Code → Download ZIP** herunterladen und entpacken (oder das Repository
   mit Git klonen). Dann die passende Anleitung öffnen:
   [Codex / ChatGPT Desktop](docs/setup-codex.md) oder [Claude Code](docs/setup-claude.md).
2. Einen separaten Ordner für deine Verkäufe anlegen, etwa „Meine-Verkaeufe“.
   Dort den Skill installieren; dieser Ordner enthält später private Daten und wird
   nicht weitergegeben. Installation funktioniert auch ohne Python per Ordnerkopie.
3. Plattformregeln klären, gegebenenfalls Browser verbinden, selbst auf der gewählten
   Verkaufsplattform anmelden und den Skill starten:
   Codex: `$sellbuddy-agent`; Claude Code: `/sellbuddy-agent`.
4. Das Interview beantworten und die Zusammenfassung bestätigen.
   Ein manueller Test kommt vor jeder regelmäßigen Automatisierung.

Startnachricht:

> Nutze SellBuddy und führe mich durch die Ersteinrichtung.
> Bitte noch nichts veröffentlichen oder versenden, bevor wir die Freigaben festgelegt haben.

## Was im Interview festgelegt wird

Ziel (schnell loswerden oder Erlös), Abholzeiten und Ausnahmen, Versand,
Datenschutz, Autonomie je Aktion, Preisuntergrenzen, Verhandlungen,
Kommunikationsstil, Benachrichtigungen und optional ein Zeitplan.
Historische eigene Nachrichten werden zur Stilanalyse nur nach gesonderter Zustimmung gelesen.
Ohne Analyse ist der Stil freundlich und knapp, ohne steife Wiederholungen.

Empfehlung: fünf Checks pro Tag um 09, 12, 15, 18 und 21 Uhr statt alle 20 Minuten.
Jeder Start benötigt Nutzungsvolumen; die tatsächliche Menge hängt von Tarif,
Verläufen und Werkzeugen ab. Nachts standardmäßig keine Starts.
Du kannst jederzeit sagen: „Automatisierung pausieren.“

## Grenzen und Sicherheit

Ein Skill ist eine Arbeitsanleitung, kein technischer Schutzmechanismus und kein
ständig laufender Dienst. Er installiert keinen Browserzugriff und erteilt keine
Plattformrechte. Ein eingerichteter Zeitplan funktioniert nur unter den Bedingungen
des jeweiligen Hosts. Rechner/App müssen für lokale Ausführung verfügbar sein.
Schlafmodus, Rechteabfragen und Anmeldeablauf können einen Lauf verhindern.
Konkrete Einstellungen und ein Funktionstest stehen unter
[Rechner wach halten: macOS und Windows](docs/keep-awake.md).

Der Agent soll Zuordnung und Ergebnisse prüfen, kann aber Fehler machen.
Starte im Entwurfsmodus und teste insbesondere Käuferzuordnung und Reservierungen.
Ein Artikel wird erst nach tatsächlicher Terminvereinbarung reserviert;
pro Artikel gibt es nur einen bestätigten Abholer.
Verfügbarkeit muss aktuell und begrenzt sein, Preiszyklen brauchen eine Untergrenze.
Keine garantierten Verkäufe und keine Garantie für Plattformzulässigkeit:
prüfe die für dich geltenden Verkaufsplattform-Regeln.

Ein eigenes Browserprofil begrenzt den Zugriff auf andere Accounts.
Passwörter und Cookies nicht exportieren. Logins und CAPTCHA selbst erledigen.
App-Berechtigungen möglichst auf benötigte Seiten und Aktionen begrenzen.
Eine Modellanweisung ersetzt diese technischen Berechtigungen nicht.

## Paket weitergeben und weiterentwickeln

Zum Weitergeben genügt der Link zum Repository. GitHub bietet unter
**Code → Download ZIP** bereits ein automatisch erzeugtes Quellcodearchiv an;
ein zusätzliches ZIP im Repository ist deshalb nicht nötig.
[GitHub-Anleitung](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives).
Deinen privaten Verkaufsordner niemals mit weitergeben.
[Datenschutz und Tests](docs/testing.md) beschreibt die Freigabeprüfung.
`share-manifest.json` enthält eine explizite Dateiliste für ein optionales Offline-ZIP:
neu hinzugefügte Dateien werden nicht automatisch aufgenommen.

Nur falls du ein separates Offline-Paket benötigst, mit Python 3.9 oder neuer im Paketordner:

```sh
python3 scripts/build_share.py --output ../sellbuddy-agent.zip
```

Eine bestehende Zieldatei wird nicht überschrieben.
Das Paket steht unter der [MIT-Lizenz](LICENSE). Die Lizenz erteilt keine
Nutzungsrechte an Verkaufsplattformen und ersetzt keine erforderliche Betreiberzustimmung.
Vor Weiterveröffentlichung Quellen/Anleitungen aktualisieren und Datenschutzprüfung wiederholen.

Stand der Einrichtungsanleitungen: 6. Oktober 2026.
Technisch validiert; nicht auf einem fremden Account oder auf beiden Hosts
durchgehend live getestet. Änderungen an App-Oberflächen können Anpassungen erfordern.
