import { createNativeStackNavigator } from "@react-navigation/native-stack";
import React from "react";
import { StyleSheet, Text, View } from "react-native";

import HomeScreen from "../../screens/HomeScreen"; 

export type RootStackParamList = {
    Home: undefined;
    Details: {
        title: string;
        description: string;
        location: string;
        hour: string;
    };
};

const Stack = createNativeStackNavigator<RootStackParamList>();

function DetailsScreen({ route }: any) {
  const { title, description, location, hour } = route.params;
  return (
    <View style={styles.detailsContainer}>
      <Text style={styles.detailsTitle}>{title}</Text>
      <View style={styles.detailsInfoBox}>
        <Text style={styles.detailsLabel}>Godzina:</Text>
        <Text style={styles.detailsValue}>{hour}</Text>
        
        <Text style={styles.detailsLabel}>Miejsce:</Text>
        <Text style={styles.detailsValue}>{location}</Text>
        
        <Text style={styles.detailsLabel}>Opis:</Text>
        <Text style={styles.detailsValue}>{description}</Text>
      </View>
    </View>
  );
}

export default function App() {
  return (
    <Stack.Navigator>
      <Stack.Screen 
        name="Home" 
        component={HomeScreen} 
        options={{ headerShown: false }} 
      />
      <Stack.Screen 
        name="Details" 
        component={DetailsScreen} 
        options={{ title: 'Szczegóły wydarzenia' }}
      />
    </Stack.Navigator>
  );
}

const styles = StyleSheet.create({
  detailsContainer: { 
    flex: 1, 
    padding: 20, 
    backgroundColor: '#4a90e2' 
  },
  detailsTitle: { 
    fontSize: 30, 
    color: 'white', 
    fontWeight: 'bold', 
    marginBottom: 20, 
    textAlign: 'center' 
  },
  detailsInfoBox: { 
    backgroundColor: 'white', 
    borderRadius: 20, 
    padding: 20, 
    elevation: 5 
  },
  detailsLabel: { 
    fontSize: 14, 
    color: '#888', 
    fontWeight: 'bold', 
    marginTop: 10 
  },
  detailsValue: { 
    fontSize: 18, 
    color: '#333', 
    marginBottom: 5 
  },
});