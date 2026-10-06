# Einrichtung: Claude Code

## 1. Browserzugriff herstellen

Der dokumentierte Weg nutzt Claude Code und die offizielle **Claude in Chrome**
Erweiterung. Die Browserfunktion benötigt einen unterstützten Anthropic-Tarif und
die direkte Claude-Anmeldung, nicht lediglich einen API-Key.
Erweiterung im gewünschten Chrome-Profil installieren.
Claude Code im Terminal starten:

```sh
claude --chrome
```

Mit `/chrome` den Verbindungsstatus prüfen und den richtigen Browser auswählen.
Zuerst die Plattformregeln und Erlaubnis klären. Erst danach die offizielle URL
der gewählten Verkaufsplattform öffnen lassen, selbst anmelden und die erforderlichen
Seitenrechte erteilen. Kein Passwort im Chat eingeben.
Bei Login/CAPTCHA soll Claude auf dich warten.
[Offizielle Chrome-Anbindung mit Voraussetzungen](https://code.claude.com/docs/en/chrome).

Falls Claude Code noch fehlt, folge der
[offiziellen Installationsanleitung](https://code.claude.com/docs/en/setup).
Installation, Tarif- und Betriebssystemvoraussetzungen dort prüfen.

## 2. Skill installieren

Einen eigenen Verkaufsordner anlegen. Den Paketordner `skills/sellbuddy-agent`
vollständig nach `Meine-Verkaeufe/.claude/skills/sellbuddy-agent` kopieren.
Alternativ aus dem entpackten Paket mit Python 3.9 oder neuer:

```sh
python3 scripts/install.py --host claude --project "/absoluter/Pfad/Meine-Verkaeufe"
```

Claude Code in diesem Verkaufsordner starten und eingeben:

```text
/sellbuddy-agent Führe mich durch die Ersteinrichtung.
```

Interview bestätigen, zunächst lesend bzw. mit einem Entwurf testen.
Projektbezogene Skills werden aus `.claude/skills` geladen.
[Offizielle Skill-Anleitung](https://code.claude.com/docs/en/skills).

## 3. Desktop statt Terminal?

In Claude Desktop den **Code**-Bereich mit deinem lokalen Verkaufsordner nutzen,
nicht einen gewöhnlichen Chat als gleichwertige Browserinstallation betrachten.
Ein eingebautes Browserfenster kann ein anderes Profil als dein eingeloggtes Chrome haben.
Prüfe in der tatsächlichen Sitzung, ob die Chrome-Anbindung verfügbar ist.
Wenn nicht, verwende den oben dokumentierten CLI-Weg.
[Claude Code Desktop](https://code.claude.com/docs/en/desktop).

## 4. Optional regelmäßige Checks

Desktop: im Code-Bereich **Routines → New routine → Local** wählen,
denselben Verkaufsordner einstellen und die bestätigten Tageszeiten konfigurieren.
Als Auftrag den Skill und die private Konfiguration nennen.
Mit **Run now** Browserzugriff und Rechte im Routinenlauf prüfen.
App offen und Rechner wach halten:
[macOS-/Windows-Einstellungen](keep-awake.md). Pausieren im Routinenstatus kontrollieren.
[Lokale Desktop-Routinen](https://code.claude.com/docs/en/desktop-scheduled-tasks).

CLI: natürliche Sprache für einen lokalen Tageszeitplan nutzen:

> Plane in dieser Sitzung Verkaufsplattform-Checks täglich um 09, 12, 15, 18 und 21 Uhr.
> Nutze /sellbuddy-agent mit der gespeicherten Konfiguration.
> Prüfe nur im vereinbarten Tagesfenster und melde Änderungen oder Handlungsbedarf.
> Zeige mir anschließend den angelegten Zeitplan.

Die Sitzung muss dafür laufen; wiederkehrende Sitzungstasks sind zeitlich begrenzt.
Ein `/loop 3h` startet nicht automatisch nur tagsüber und ersetzt keinen dauerhaften
Dienst. Verwende es höchstens für eine bewusst begrenzte aktive Sitzung.
Geplante Starts können verzögert sein.
[CLI-Zeitplanung und Grenzen](https://code.claude.com/docs/en/scheduled-tasks).

Nicht gleichzeitig Desktop-Routine und CLI-Loop für denselben Account starten.
Kein `/clear` mitten in ungespeicherten Browserentwürfen; Sitzungstabs können betroffen sein.
