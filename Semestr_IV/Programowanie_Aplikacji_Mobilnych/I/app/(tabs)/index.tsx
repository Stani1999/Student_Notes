import { styles } from "@/styles/IndexStyles";
import { RootStackParamList } from "@/types/Navigation";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import React from "react";
import { Text, View } from "react-native";
import HomeScreen from "../../screens/HomeScreen";


const Stack = createNativeStackNavigator<RootStackParamList>();

function DetailsScreen({ route }: any) {
  const { title, description, location, hour, date, category } = route.params;
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

        <Text style={styles.detailsLabel}>Godzina:</Text>
        <Text style={styles.detailsValue}>{hour}</Text>

        <Text style={styles.detailsLabel}>Data:</Text>
        <Text style={styles.detailsValue}>{date}</Text>

        <Text style={styles.detailsLabel}>Kategoria:</Text>
        <Text style={styles.detailsValue}>{category}</Text>
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