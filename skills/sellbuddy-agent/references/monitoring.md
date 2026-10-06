# Wiederkehrende Checks

Der Skill läuft nicht von selbst. Verwende die native Zeitplanung des Hosts,
keinen improvisierten Hintergrundprozess und keine langen Schlafschleifen im Chat.
Einrichtung nur mit ausdrücklichem Auftrag; zuerst vorhandene passende Automation
finden und aktualisieren statt eine zweite anzulegen.

## Vor Einrichtung

setup_complete, geklärte Plattform-Erlaubnis, Freigaben, Zeitzone, Tagesfenster, Enddatum, Verfügbarkeit und persistente
Dateien prüfen. Manuellen Lauf testen. Browserrechte können in geplanten Läufen anders
sein; ersten geplanten Lauf oder „Run now“ prüfen. Vor diesem Test nur „eingerichtet,
noch nicht im geplanten Lauf verifiziert“ melden.

Codex/ChatGPT Desktop: wenn verfügbar eine lokale wiederkehrende Folgeaktion in
diesem Chat verwenden; native Automationswerkzeuge nutzen. Rechner wach und App offen.
Nicht auf Cloud-Ausführung wechseln, wenn die lokale eingeloggte Browsersitzung nötig ist.

Claude Code: native lokale Routinen der Desktop-App oder die dokumentierte
Sitzungszeitplanung im CLI verwenden. Bei Desktop-Routinen denselben privaten
Arbeitsordner wählen, keine isolierte Worktree-Kopie. Frische Läufe müssen den
Browserzugriff selbst herstellen können: „Run now“ testen.
CLI-Zeitpläne benötigen eine laufende Sitzung. Ein /loop allein ist weder
dauerhaft noch automatisch auf Tageszeiten begrenzt.

Bevorzugt konkrete Tagesstarts planen (z.B. 09, 12, 15, 18, 21 Uhr).
Nur eine Nachtprüfung im Prompt verhindert Browseraktionen, aber nicht den
Modellaufruf selbst und spart daher nicht sämtliche Nutzung.
Zeitplanung ist nicht minutengenau und kann bei Schlafmodus ausfallen.

## Auftrag für den geplanten Lauf

Mit tatsächlichen bestätigten Einstellungen statt erfundenen Werten formulieren:

„Nutze den SellBuddy-Skill. Lies im vereinbarten Arbeitsordner die private
Konfiguration und Verkaufsübersicht. Prüfe aktuelle lokale Zeit, Pausenstatus und
Gültigkeit. Außerhalb der freigegebenen Zeiten oder bei pausiertem Monitoring keine
Browseraktionen ausführen. Prüfe aktuelle Anfragen, beantworte sie nur innerhalb der
Freigaben, halte pro Artikel genau eine bestätigte Abholung und führe fällige
Preisänderungen nur innerhalb der artikelbezogenen Grenzen aus. Verifiziere Aktionen
und aktualisiere die Übersicht. Berichte gemäß Benachrichtigungsregel; bei unveränderter
Lage still bleiben, sofern keine regelmäßige Übersicht ausdrücklich gewünscht ist.“

## Je Lauf

1. Konfiguration, Ledger und aktuelle Zeit lesen; Plattform-Erlaubnis, Pausenstatus, Tagesfenster und
   Enddatum prüfen. Abgelaufene Verfügbarkeit nicht als Zusagegrundlage verwenden.
2. Überlappenden laufenden Check ausschließen. Bei Unklarheit diesen Lauf überspringen.
3. Neue/aktuelle relevante Nachrichten prüfen, unsichere frühere Aktionen abgleichen,
   freigegebene Antworten senden und Abholungen aktualisieren.
4. Fällige Preisregeln prüfen; Reservierungen und Untergrenzen beachten.
5. Offene Bewertungen bestätigter Verkäufe nur bei Freigabe prüfen, nicht alle alten
   Chats bei jedem Lauf erneut öffnen.
6. Erfolge und offene Punkte speichern; nach gewählter Regel berichten.

Bei Loginablauf, fehlenden Rechten, CAPTCHA oder nicht erreichbarer Oberfläche keine
leere Inbox behaupten. Einen sicheren Verbindungsversuch machen, dann Einschränkung
melden und auf Nutzeraktion warten. Keine dauernden Wiederholungsversuche.

## Pausieren

Bei „pausieren“ monitoring.enabled=false speichern UND die tatsächliche native
Automation pausieren. Erfolg des Host-Werkzeugs überprüfen. Falls das Werkzeug fehlt,
den lokalen Ausführungsschutz setzen und klar sagen, dass der Host-Zeitplan noch
manuell deaktiviert werden muss. Nicht eigenständig wieder aktivieren.
