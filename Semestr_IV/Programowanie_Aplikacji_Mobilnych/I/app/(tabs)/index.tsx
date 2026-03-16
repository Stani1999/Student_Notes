import React, { useState, useRef } from 'react';
import { Alert, Modal, StyleSheet, Text, Pressable, View, Animated } from 'react-native';
import { SafeAreaView, SafeAreaProvider } from 'react-native-safe-area-context';

const MAX_PRESSES = 67;
const OPONENT = "Wróg";
const OPONENT_DISCRIBE = "Wrogów"
const HOLD_DURATION = 3000; // 3 sekund w milisekundach

const App = () => {
  const [modalVisible, setModalVisible] = useState(false);
  const [count, setCount] = useState(0);

  // Animacja paska (wartość od 0 do 1)
  const progress = useRef(new Animated.Value(0)).current;

  const handlePress = () => {
    const newCount = count + 1;
    setCount(newCount);

    if (newCount === MAX_PRESSES) {
      Alert.alert('Przestań proszę');
      setModalVisible(true);
    }
  };

  // Rozpoczęcie trzymania przycisku
  const startHolding = () => {
    Animated.timing(progress, {
      toValue: 1,
      duration: HOLD_DURATION,
      useNativeDriver: false, // false, bo animujemy szerokość (width)
    }).start(({ finished }) => {
      // Jeśli animacja dobiegła końca (5s minęło)
      if (finished) {
        resetApp();
      }
    });
  };

  // Przerwanie trzymania - reset paska do zera
  const stopHolding = () => {
    Animated.timing(progress).stop();
    Animated.timing(progress, {
      toValue: 0,
      duration: 300,
      useNativeDriver: false,
    }).start();
  };

  const resetApp = () => {
    setModalVisible(false);
    setCount(0);
    progress.setValue(0);
  };

  // Mapowanie wartości animacji na procentową szerokość paska
  const progressWidth = progress.interpolate({
    inputRange: [0, 1],
    outputRange: ['0%', '100%'],
  });

  return (
    <SafeAreaProvider>
      <SafeAreaView style={styles.centeredView}>
        
        <View style={styles.header}>
          <Text style={styles.title}>Smart Campus</Text>
          <Text style={styles.infoText}>{OPONENT} przed tobą!!! Zrób coś</Text>
          <Text style={styles.infoText}>Licznik uderzeń w {OPONENT_DISCRIBE}: {count} / {MAX_PRESSES}</Text>
        </View>

        <Modal
          animationType="fade"
          transparent={true}
          visible={modalVisible}
          onRequestClose={() => setModalVisible(false)}>
          <View style={styles.centeredView}>
            <View style={styles.modalView}>
              <Text style={styles.modalText}>Uderzyłeś mnie {MAX_PRESSES} razy...</Text>
              
              <Text style={styles.instruction}>Przytrzymaj, aby zresetować:</Text>

              {/* Przycisk z paskiem postępu */}
              <Pressable
                onPressIn={startHolding}
                onPressOut={stopHolding}
                style={styles.holdButtonContainer}>
                
                {/* Warstwa tła paska postępu */}
                <Animated.View style={[styles.progressBar, { width: progressWidth }]} />
                
                {/* Tekst na wierzchu */}
                <Text style={styles.holdButtonText}>"Ja chceeee jeeeszczeeee razzzz"</Text>
              </Pressable>
            </View>
          </View>
        </Modal>

        <Pressable
          style={({ pressed }) => [
            styles.button,
            styles.buttonOpen,
            pressed && styles.buttonPressed
          ]}
          onPress={handlePress}>
          <Text style={styles.textStyle}>BIJ!!!</Text>
        </Pressable>

      </SafeAreaView>
    </SafeAreaProvider>
  );
};

const styles = StyleSheet.create({
  centeredView: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f5f6fa',
  },
  header: {
    position: 'absolute',
    top: 70,
    alignItems: 'center',
  },
  title: {
    fontSize: 30,
    fontWeight: 'bold',
    color: '#2c3e50',
    marginBottom: 8,
  },
  infoText: {
    fontSize: 16,
    color: '#95a5a6',
    fontWeight: '500',
  },
  modalView: {
    width: '90%',
    backgroundColor: 'white',
    borderRadius: 25,
    padding: 30,
    alignItems: 'center',
    elevation: 10,
  },
  modalText: {
    fontSize: 20,
    color: '#2c3e50',
    marginBottom: 5,
  },
  instruction: {
    fontSize: 14,
    color: '#7f8c8d',
    marginBottom: 20,
  },
  // Style przycisku trzymania
  holdButtonContainer: {
    width: '100%',
    height: 65,
    backgroundColor: '#ecf0f1',
    borderRadius: 15,
    justifyContent: 'center',
    alignItems: 'center',
    overflow: 'hidden', // Kluczowe, by pasek nie wystawał poza zaokrąglenia
    borderWidth: 1,
    borderColor: '#dcdde1',
  },
  progressBar: {
    position: 'absolute',
    left: 0,
    top: 0,
    bottom: 0,
    backgroundColor: '#3498db', // Kolor ładującego się paska
  },
  holdButtonText: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#2c3e50',
    textAlign: 'center',
    zIndex: 1, // Tekst musi być nad paskiem
  },
  // Style głównego przycisku
  button: {
    borderRadius: 30,
    paddingVertical: 18,
    paddingHorizontal: 45,
    elevation: 4,
  },
  buttonOpen: {
    backgroundColor: '#e74c3c',
  },
  buttonPressed: {
    backgroundColor: '#c0392b',
    transform: [{ scale: 0.96 }],
  },
  textStyle: {
    color: 'white',
    fontWeight: 'bold',
    fontSize: 22,
    textAlign: 'center',
  },
});

export default App;
