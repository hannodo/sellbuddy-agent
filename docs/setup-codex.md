# Einrichtung: Codex / ChatGPT Desktop

## 1. Lokalen Browser verbinden

Aktuelle Desktop-App öffnen. Unter **Settings → Computer Use** den gewünschten
Browser aktivieren. Falls eine Erweiterung verlangt wird, **Install** wählen,
im richtigen Chrome-Profil installieren und anschließend die Verbindung prüfen.
In einer lokalen Work-/Codex-Aufgabe den Browser über **@Chrome** auswählen.
Zuerst die Erlaubnis der gewählten Verkaufsplattform für die gewünschte Nutzung
klären. Erst danach deren offizielle URL öffnen und den Anmeldestatus prüfen lassen.
Du meldest dich selbst an. Seitenrechte gezielt freigeben.

Bei Problemen: richtige Browserprofilauswahl prüfen, Erweiterung aktivieren,
App/Browser neu starten und in einem neuen Chat testen. Für Foto-Uploads kann
in den Erweiterungsdetails „Allow access to file URLs“ nötig sein.
Fehlt die Funktion in deiner App, nicht von vorhandenen Computer-Use-Rechten ausgehen.
[Offizielle Browser-Anleitung](https://learn.chatgpt.com/docs/chrome-extension).

## 2. Skill in deinen Verkaufsordner laden

Ordner „Meine-Verkaeufe“ als lokales Projekt öffnen/hinzufügen.
Kopiere den kompletten Paketordner `skills/sellbuddy-agent` nach:

```text
Meine-Verkaeufe/
  .agents/
    skills/
      sellbuddy-agent/
        SKILL.md
        agents/
        references/
        assets/
```

Versteckte Ordner müssen eventuell im Dateimanager eingeblendet werden.
Alternativ im Terminal aus dem entpackten Paket:

```sh
python3 scripts/install.py --host codex --project "/absoluter/Pfad/Meine-Verkaeufe"
```

Der Installer benötigt Python 3.9 oder neuer, überschreibt keinen vorhandenen Skill und installiert
nur in diesen Ordner. Ohne Python genügt die Ordnerkopie.
Codex-Aufgabe im Verkaufsordner starten und `$sellbuddy-agent` eingeben.
Falls der Skill nicht erscheint, die App neu starten.
[Offizielle Skill-Anleitung](https://learn.chatgpt.com/docs/build-skills).

In einer ChatGPT-Desktop-Umgebung ohne lokale Skill-Erkennung nicht einfach den ZIP-Upload
als Installation betrachten. Nutze eine lokale Codex-Aufgabe mit dem Verkaufsordner.

## 3. Interview und Test

Die Startnachricht aus der README senden. Der Agent fragt nach deinen Regeln und
speichert private Konfiguration und Verkaufsübersicht im Verkaufsordner.
Teste zunächst eine Anzeige als Entwurf und einen Nachrichtencheck nur lesend.
Prüfe, ob Artikel und Gespräche richtig zugeordnet sind. Dann gewünschte Aktionen freigeben.

## 4. Optional regelmäßig prüfen

Nach erfolgreichem Test etwa sagen:

> Prüfe in dieser lokalen Aufgabe täglich um 09, 12, 15, 18 und 21 Uhr die
> Verkaufsplattform-Anfragen nach meiner gespeicherten Konfiguration.
> Richte dafür eine wiederkehrende Folgeaktion ein. Melde nur Änderungen oder Handlungsbedarf.

Vorhandenen passenden Zeitplan aktualisieren lassen, keinen zweiten anlegen.
App offen und Rechner wach halten:
[macOS-/Windows-Einstellungen](keep-awake.md). Den ersten geplanten Lauf prüfen; Browserrechte
können noch eine Bestätigung brauchen. Eine Zeitplanung allein beweist keinen Browserzugriff.
Pausieren mit „Automatisierung pausieren“ und den Status kontrollieren.
[Offizielle Automations-Anleitung](https://learn.chatgpt.com/docs/automations).
