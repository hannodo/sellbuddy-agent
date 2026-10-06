# Rechner für regelmäßige Checks wach halten

**Eingeschaltet allein genügt nicht:** Während der geplanten Checks muss der Rechner
wach sein, Internet haben und die Agent-App samt Browser verfügbar sein.
Bei Claude-Code-CLI muss auch die Sitzung weiterlaufen.
Du kannst den Agenten nachts pausieren; es ist kein 24-Stunden-Betrieb nötig.
Nach Neustart oder Update prüfen, ob App, Browser und Zeitplan wieder bereit sind.

Am einfachsten: Netzteil anschließen und Laptopdeckel offen lassen.
Das Ausschalten des Displays ist nicht dasselbe wie Standby/Ruhezustand.
Eine Bildschirmsperre ist wiederum etwas anderes: Ob Browserwerkzeuge damit weiter
funktionieren, hängt vom Host ab und muss getestet werden.
Passwortschutz nicht pauschal deaktivieren. Bei gesperrter Sitzung nötige Freigaben
nicht umgehen, sondern entsperren oder den Betrieb pausieren.

## macOS

MacBook: **Apple-Menü → Systemeinstellungen → Batterie → Optionen**.
Die Option **„Kein automatisches Aktivieren des Ruhezustands im Netzbetrieb bei
ausgeschaltetem Display“** aktivieren.

Desktop-Mac: unter **Systemeinstellungen → Energie** die entsprechende Option zum
Verhindern des automatischen Ruhezustands bei ausgeschaltetem Display aktivieren.
Je nach macOS-Version heißen diese Bereiche anders, etwa „Energie sparen“.
Die Systemeinstellungen-Suche hilft; manche Optionen hängen vom Modell ab.

Display-Abschaltung kannst du separat unter **Sperrbildschirm** konfigurieren.
Den Mac nicht manuell in den Ruhezustand versetzen.
[Apple-Anleitung](https://support.apple.com/de-de/guide/mac-help/-mchle41a6ccd/mac).

Für die einfache Einrichtung den MacBook-Deckel offen lassen.
Nicht annehmen, dass die Netzbetrieb-Einstellung auch Zuklappen verhindert.
Geschlossener Betrieb mit externem Bildschirm ist ein eigener, modellabhängiger
Betriebsmodus und kein notwendiger Teil dieses Setups.

## Windows 11

**Start → Einstellungen → System → Stromversorgung und Akku** öffnen
(je nach Version auch „Netzbetrieb und Akku“).
Unter **Bildschirm-, Energiespar- und Ruhezustandstimeouts** die automatische
Standby-/Ruhezustandszeit für **Netzbetrieb** auf **Nie** stellen.
Alle dort angebotenen Schlaf-/Ruhezustandstimer für Netzbetrieb prüfen.
Display-Abschaltung kann separat eingestellt bleiben.
[Microsoft-Anleitung](https://support.microsoft.com/de-de/windows/experience/power-battery/power-settings-in-windows-11).

Bei älteren Windows-Oberflächen findet sich die Einstellung unter
**System → Netzbetrieb und Energiesparen** oder in den **Energieoptionen**
der Systemsteuerung. Die Einstellungen-Suche nach „Energiesparmodus“ hilft.

Auch unter Windows löst Zuklappen oft Standby aus. Empfehlung: Deckel offen lassen.
Falls du ihn geschlossen nutzen möchtest, in
**Systemsteuerung → Hardware und Sound → Energieoptionen → Auswählen, was beim
Zuklappen des Computers geschehen soll** für Netzbetrieb **Nichts unternehmen**
wählen, sofern angeboten. Herstellereinstellungen können abweichen.
[Microsoft zu Standby und Deckelverhalten](https://support.microsoft.com/de-de/windows/experience/power-battery/shut-down-sleep-or-hibernate-your-pc).

## Abschlusstest

1. Einen Testlauf für etwa 10–15 Minuten später planen.
2. Rechner nicht bedienen; gewählte Display-/Sperreinstellungen wirken lassen.
3. Prüfen, ob der Lauf wirklich neue Browserdaten gelesen hat – eine bloße
   Zeitplan-Benachrichtigung beweist das nicht.
4. Bei Bedarf entsperren und erneut testen. Keine Sicherheitseinstellungen
   blind abschalten. Bei Firmenrechnern können Richtlinien Änderungen verhindern.

Dauerhaftes Wachhalten erhöht Stromverbrauch. Gerät gut belüftet betreiben,
nicht eingeschaltet in eine Tasche legen. Nach Ende des Verkaufsprojekts
Monitoring pausieren und normale Energiespareinstellungen wiederherstellen.
Diese Anleitung ändert keine Systemeinstellungen automatisch.
