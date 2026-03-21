import React from 'react';
import { View, StyleSheet, ScrollView } from "react-native";
import { Header } from "../../components/Header"; 
import ListItem from "../../components/ListItem";

export default function HomeScreen() {
  const events = [
    { id: 1, title: "Wykład React", description: "Dzień 1 - 10:00", location: "Sala A1", isHighlighted: true },
    { id: 2, title: "Warsztaty AI", description: "Dzień 1 - 12:00", location: "Sala B2", isHighlighted: false },
    { id: 3, title: "Spotkanie koła", description: "Dzień 1 - 15:00", location: "Sala C3", isHighlighted: false },
    { id: 4, title: "Pizza Time", description: "Dzień 1 - 16:00", location: "Sala 69a", isHighlighted: false },
    { id: 5, title: "Networking", description: "Dzień 1 - 16:30", location: "Aula GM", isHighlighted: false },
    { id: 6, title: "Wykład React", description: "Dzień 2 - 10:00", location: "Sala A1", isHighlighted: true },
    { id: 7, title: "Warsztaty AI", description: "Dzień 2 - 12:00", location: "Sala B2", isHighlighted: false },
    { id: 8, title: "Spotkanie koła", description: "Dzień 2 - 15:00", location: "Sala C3", isHighlighted: false },
    { id: 9, title: "Pizza Time", description: "Dzień 2 - 16:00", location: "Sala 69a", isHighlighted: false },
    { id: 10, title: "Networking", description: "Dzień 2 - 16:30", location: "Aula GM", isHighlighted: false }  ];

  return (
    <View style={styles.container}>
      <Header title="Smart Campus" />
      
      <ScrollView>
        {events.map((event) => (
          <ListItem 
            key={event.id} 
            title={event.title} 
            description={event.description} 
            location={event.location}
            isHighlighted={event.isHighlighted}
          />
        ))}
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#f2f2f2",
    paddingTop: 50,
  },
});