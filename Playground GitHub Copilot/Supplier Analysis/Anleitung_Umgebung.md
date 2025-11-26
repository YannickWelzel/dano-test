# Anleitung: Virtuelle Python-Umgebung (dano-env)

Diese Anleitung erklärt, wie Sie die virtuelle Umgebung für das Analyse-Projekt aktivieren und deaktivieren.

### Was ist das?

Eine virtuelle Umgebung ist wie eine saubere, isolierte "Werkzeugkiste" nur für dieses Projekt. Pakete, die wir hier installieren, stören nicht Ihre Haupt-Python-Installation und umgekehrt.

---

### Umgebung vor der Arbeit AKTIVIEREN

Bevor Sie das Jupyter Notebook `Supplier_Analysis.ipynb` verwenden, müssen Sie **immer zuerst** die Umgebung in einem neuen VS Code Terminal aktivieren. Der Befehl hängt von Ihrem Terminal ab.

1.  Öffnen Sie ein neues Terminal in VS Code (`Terminal` > `New Terminal`).
2.  Führen Sie den passenden Befehl aus:

    **Für PowerShell (Standard in VS Code):**
    ```shell
    C:\venvs\dano-env\Scripts\Activate.ps1
    ```

    **Für Git Bash (wenn Sie `bash` verwenden):**
    ```shell
    source /c/venvs/dano-env/Scripts/activate
    ```

3.  Die Terminal-Zeile zeigt nun `(dano-env)` am Anfang an. Das bedeutet, die Umgebung ist aktiv.

**Wichtig für VS Code:** Wenn Sie das Notebook zum ersten Mal mit der neuen Umgebung öffnen, klicken Sie oben rechts auf **"Select Kernel"** und wählen Sie den Python-Interpreter aus, der auf `C:\venvs\dano-env` verweist.

---

### Umgebung nach der Arbeit DEAKTIVIEREN

Wenn Sie fertig sind, können Sie die Umgebung mit einem einfachen Befehl wieder verlassen:

1.  Geben Sie in das aktive Terminal ein:

    ```shell
    deactivate
    ```
2.  Das `(dano-env)` am Anfang der Zeile verschwindet.
