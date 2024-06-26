# KeysStore

Open Source Tool for creating **Android KeyStore**, **Sign your App Build** with your keystore & **Install your Android Build** without using **Android Studio** on your device.

![app](/assets/app.png)

## Fixtures

- Generate new Android Keystore (*.keystore)
- Sign your app build(s) (*.aab)
- Install **builds** to your device

## Dependencies

> **Note:** This program depends on the following software's, so make sure you install them before using the program.

- [Java Development Kit](https://www.oracle.com/java/technologies/downloads/)
- [ADB (Android Debug Bridge)](https://developer.android.com/tools/releases/platform-tools)
- [Bundletool](https://github.com/google/bundletool/releases)

## How to install?

    git clone https://github.com/budzhors7/keysstore

Open project directory

    cd keysstore

Install python requirements

***Windows***

    pip install -r requirements.txt

***MacOS***

    pip3 install -r requirements.txt

To run the program

> Make sure you've downloaded [Bundletool](https://github.com/google/bundletool/releases), rename the file to bundletool.jar & insert the file in the **lib** folder.

***Windows***

    python app.py

***MacOS***

    python3 app.py
