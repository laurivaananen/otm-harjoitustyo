package com.mycompany.unicafe;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;


public class KassapaateTest {
    
    Kassapaate kassapaate;
    Maksukortti maksukortti;
    
    public KassapaateTest() {
    }
    
    @BeforeClass
    public static void setUpClass() {
    }
    
    @AfterClass
    public static void tearDownClass() {
    }
    
    @Before
    public void setUp() {
        kassapaate = new Kassapaate();
        maksukortti = new Maksukortti(0);
    }
    
    @After
    public void tearDown() {
    }

    // TODO add test methods here.
    // The methods must be annotated with annotation @Test. For example:
    //
    // @Test
    // public void hello() {}
    
    @Test
    public void kassassaRahaaOikeaMaara() {
        assertEquals(100000, kassapaate.kassassaRahaa());
    }
    
    @Test
    public void edullisiaLounaitaMyytyOikeaMaara() {
        assertEquals(0, kassapaate.edullisiaLounaitaMyyty());
    }
    
    @Test
    public void maukkaitaLounaitaMyytyOikeaMaara() {
        assertEquals(0, kassapaate.maukkaitaLounaitaMyyty());
    }
    
    @Test
    public void syoEdullisestiKasvattaaKassanRahaMaaraaOikeanVerran() {
        kassapaate.syoEdullisesti(250);
        assertEquals(100240, kassapaate.kassassaRahaa());
    }
    
    @Test
    public void syoMaukkaastiKasvattaaKassanRahaMaaraaOikeanVerran() {
        kassapaate.syoMaukkaasti(500);
        assertEquals(100400, kassapaate.kassassaRahaa());
    }
    
    @Test
    public void syoEdullisestiAntaaOikeanVerranVaihtoRahaa() {
        assertEquals(25, kassapaate.syoEdullisesti(265));
    }
    
    @Test
    public void syoMaukkaastiAntaaOikeanVerranVaihtoRahaa() {
        assertEquals(25, kassapaate.syoMaukkaasti(425));
    }
    
    @Test
    public void syoEdullisestiKasvattaaMyytyjenLounaidenMaaraaJosMaksuOnRiittava() {
        kassapaate.syoEdullisesti(240);
        assertEquals(1, kassapaate.edullisiaLounaitaMyyty());
    }
    
    @Test
    public void syoEMaukkaastiKasvattaaMyytyjenLounaidenMaaraaJosMaksuOnRiittava() {
        kassapaate.syoMaukkaasti(400);
        assertEquals(1, kassapaate.maukkaitaLounaitaMyyty());
    }
    
    @Test
    public void syoEdullisestiEiKasvataMyytyjenLounaidenMaaraaJosMaksuEiOleRiittava() {
        kassapaate.syoEdullisesti(239);
        assertEquals(0, kassapaate.edullisiaLounaitaMyyty());
    }
    
    @Test
    public void syoMaukkaastiEiKasvataMyytyjenLounaidenMaaraaJosMaksuEiOleRiittava() {
        kassapaate.syoMaukkaasti(399);
        assertEquals(0, kassapaate.maukkaitaLounaitaMyyty());
    }
    
    @Test
    public void kaikkiRahatPalautetaanVaihtorahanaJosMaksuEiOllutRiittavaEdulliseenLounaaseen() {
        assertEquals(15, kassapaate.syoEdullisesti(15));
    }
    
    @Test
    public void kaikkiRahatPalautetaanVaihtorahanaJosMaksuEiOllutRiittavaMaukkaaseenLounaaseen() {
        assertEquals(15, kassapaate.syoMaukkaasti(15));
    }
    
    @Test
    public void syoEdullisestiKortillaKasvattaaMyytyjenLounaidenMaaraaJosMaksuOnRiittava() {
        maksukortti.lataaRahaa(1000);
        kassapaate.syoEdullisesti(maksukortti);
        assertEquals(1, kassapaate.edullisiaLounaitaMyyty());
    }
    
    @Test
    public void syoEMaukkaastiKortillaKasvattaaMyytyjenLounaidenMaaraaJosMaksuOnRiittava() {
        maksukortti.lataaRahaa(1000);
        kassapaate.syoMaukkaasti(maksukortti);
        assertEquals(1, kassapaate.maukkaitaLounaitaMyyty());
    }
    
    @Test
    public void syoEdullisestiKortillaPalauttaaTrueJosMaksuOnRiittava() {
        maksukortti.lataaRahaa(1000);
        assertEquals(true, kassapaate.syoEdullisesti(maksukortti));
    }
    
    @Test
    public void syoMaukkaastiKortillaPalauttaaTrueJosMaksuOnRiittava() {
        maksukortti.lataaRahaa(1000);
        assertEquals(true, kassapaate.syoMaukkaasti(maksukortti));
    }
    
    @Test
    public void syoEdullisestiKortillaPalauttaaFalseJosMaksuOnRiittava() {
        maksukortti.lataaRahaa(0);
        assertEquals(false, kassapaate.syoEdullisesti(maksukortti));
    }
    
    @Test
    public void syoMaukkaastiKortillaPalauttaaFalseJosMaksuOnRiittava() {
        maksukortti.lataaRahaa(0);
        assertEquals(false, kassapaate.syoMaukkaasti(maksukortti));
    }
    
    @Test
    public void syoEdullisestiKortillaVeloittaaSummanJosMaksuOnRiittava() {
        maksukortti.lataaRahaa(1000);
        kassapaate.syoEdullisesti(maksukortti);
        assertEquals(760, maksukortti.saldo());
    }
    
    @Test
    public void syoMaukkaastiKortillaVeloittaaSummanJosMaksuOnRiittava() {
        maksukortti.lataaRahaa(1000);
        kassapaate.syoMaukkaasti(maksukortti);
        assertEquals(600, maksukortti.saldo());
    }
    
    @Test
    public void syoEdullisestiKortillaEiVeloitaSummanJosMaksuEiOleRiittava() {
        maksukortti.lataaRahaa(100);
        kassapaate.syoEdullisesti(maksukortti);
        assertEquals(100, maksukortti.saldo());
    }
    
    @Test
    public void syoMaukkaastiKortillaEiVeloitaSummanJosMaksuEiOleRiittava() {
        maksukortti.lataaRahaa(100);
        kassapaate.syoMaukkaasti(maksukortti);
        assertEquals(100, maksukortti.saldo());
    }
    
    @Test
    public void syoEdullisestiKortillaEiKasvataMyytyjenLounaidenMaaraaJosMaksuEiOllutRiittava() {
        maksukortti.lataaRahaa(100);
        kassapaate.syoEdullisesti(maksukortti);
        assertEquals(0, kassapaate.edullisiaLounaitaMyyty());
    }
    
    @Test
    public void syoMaukkaastiKortillaEiKasvataMyytyjenLounaidenMaaraaJosMaksuEiOllutRiittava() {
        maksukortti.lataaRahaa(100);
        kassapaate.syoMaukkaasti(maksukortti);
        assertEquals(0, kassapaate.maukkaitaLounaitaMyyty());
    }
    
    @Test
    public void KassassaOlevaRahamaaraEiMuutuKortillaOstaessaEdullinenLounas() {
        maksukortti.lataaRahaa(1000);
        kassapaate.syoEdullisesti(maksukortti);
        assertEquals(100000, kassapaate.kassassaRahaa());
    }
    
    @Test
    public void KassassaOlevaRahamaaraEiMuutuKortillaOstaessaMaukasLounas() {
        maksukortti.lataaRahaa(1000);
        kassapaate.syoMaukkaasti(maksukortti);
        assertEquals(100000, kassapaate.kassassaRahaa());
    }
    
    @Test
    public void kortillaRahaaLadatessaKassassaOlevaRahamaaraKasvaa() {
        kassapaate.lataaRahaaKortille(maksukortti, 25);
        assertEquals(100025, kassapaate.kassassaRahaa());
    }
    
    @Test
    public void kortillaRahaaLadatessaKassassaOlevaRahamaaraEiKasvaJosLadataanNegatiivinenSumma() {
        kassapaate.lataaRahaaKortille(maksukortti, -100);
        assertEquals(100000, kassapaate.kassassaRahaa());
    }
    
    
    
    
}
