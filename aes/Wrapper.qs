namespace Wrapper {
    open QTests.AES;

    operation SmartWideRijndaelWrapper() : Unit {
        let Nr = 10;
        let Nk = 4;
        let inPlaceMixcolumn = true;
        let freeSwaps = true;
        let message = [Zero, size = 128];
        let key = [Zero, size = 32 * Nk];
        let _ = SmartWideRijndael(message, key, Nr, Nk, inPlaceMixcolumn, freeSwaps);
    }
}