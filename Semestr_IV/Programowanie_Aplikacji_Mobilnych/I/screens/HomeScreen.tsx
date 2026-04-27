import { events as initialEvents } from "@/data/event";
import { Event } from "@/types/Event";
import { styles } from "@/styles/HomeScreenStyles";
import { NativeStackNavigationProp } from "@react-navigation/native-stack";
import React, { useState } from "react";
import {
    Button,
    FlatList,
    Modal,
    Text,
    View
} from "react-native";

import { RootStackParamList } from "@/types/Navigation";
import ListItem from "../components/ListItem";
import AddEventForm from "@/components/AddEventForm";

type HomeScreenProps = {
    navigation: NativeStackNavigationProp<RootStackParamList, "Home">; 
}

export default function HomeScreen({ navigation }: HomeScreenProps) {
    const [events, setEvents] = useState<Event[]>(initialEvents);

    const addEvent = (newEvent: Omit<Event, "id">) => {
        const eventToAdd: Event = {
            id: Date.now(),
            ...newEvent,
        };

        setEvents((prevEvents) => [eventToAdd, ...prevEvents]);
    };

    const [count, setCount] = useState(0);
    const [modalVisible, setModalVisible] = useState(false);

    const handlePress = () => {
        const nextCount = count + 1;
        setCount(nextCount);
        if (nextCount > 4) setModalVisible(true);
    };

    return (
        <View style={styles.container}>
            <AddEventForm onAddEvent={addEvent}/>
            <FlatList
                data={events}
                keyExtractor={(item) => item.id.toString()}
                ListHeaderComponent={
                    <>
                        <View style={styles.counterSection}>
                            <Text style={styles.counterText}>Licznik: {count}</Text>
                            <Button title="Zwiększ" onPress={handlePress} />
                        </View>
                        <Text style={styles.header}>Wydarzenia</Text>
                    </>
                }
                renderItem={({ item }: { item: Event }) => (
                    <ListItem 
                        title={item.title}
                        description={item.description}
                        location={item.location}
                        hour={item.hour}
                        date={item.date}
                        category={item.category}
                        speaker={item.speaker}
                        isWorkshop={item.category === "Warsztaty"}
                        isHighlighted={item.id % 2 === 0}
                        onPress={() => navigation.navigate("Details", {
                            title: item.title,
                            description: item.description,
                            location: item.location,
                            hour: item.hour,
                            date: item.date,
                            category: item.category,
                            speaker: item.speaker,
                        })}
                    />
                )}
            />

            <Modal
                animationType="fade"
                transparent={true}
                visible={modalVisible}
                onRequestClose={() => setModalVisible(false)}
            >
                <View style={styles.centeredView}>
                    <View style={styles.modalView}>
                        <Text style={styles.modalTitle}>Limit kliknięć!</Text>
                        <Text>Kliknąłeś już {count} razy.</Text>
                        <Button title="Zamknij" onPress={() => setModalVisible(false)} />
                    </View>
                </View>
            </Modal>
        </View>
    );
}