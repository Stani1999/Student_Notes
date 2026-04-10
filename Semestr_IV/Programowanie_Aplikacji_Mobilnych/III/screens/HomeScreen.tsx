import { NativeStackNavigationProp } from "@react-navigation/native-stack";
import React, { useState } from "react";
import {
    Button,
    Modal,
    FlatList,
    StyleSheet,
    Text,
    View
} from "react-native";

import { RootStackParamList } from "../app/(tabs)/index";
import ListItem from "../components/ListItem";

type HomeScreenProps = {
    navigation: NativeStackNavigationProp<RootStackParamList, "Home">; 
}

interface EventItem {
    id: number;
    title: string;
    description: string;
    location: string;
    hour: string;
}

export default function HomeScreen({ navigation }: HomeScreenProps) {
    const [count, setCount] = useState(0);
    const [modalVisible, setModalVisible] = useState(false);

    const events: EventItem[] = [
        { id: 1, title: "Wykład React Native", description: "Sala A1, 10:00", location: "Sala A1", hour: "10:00" },
        { id: 2, title: "Warsztaty AI", description: "Sala B2, 12:00", location: "Sala B2", hour: "12:00" },
        { id: 3, title: "Spotkanie koła", description: "Sala C3, 15:00", location: "Sala C3", hour: "15:00" },
        { id: 4, title: "Konferencja Tech", description: "Aula Główna, 09:00", location: "Aula Główna", hour: "09:00" },
        { id: 5, title: "Mecz Koszykówki", description: "Hala Sportowa, 17:30", location: "Hala Sportowa", hour: "17:30" },
    ];

    const handlePress = () => {
        const nextCount = count + 1;
        setCount(nextCount);
        if (nextCount > 4) setModalVisible(true);
    };

    return (
        <View style={styles.container}>
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
                renderItem={({ item }) => (
                    <ListItem 
                        title={item.title}
                        description={item.description}
                        location={item.location}
                        isHighlighted={item.id % 2 === 0}
                        onPress={() => navigation.navigate("Details", {
                            title: item.title,
                            description: item.description,
                            location: item.location,
                            hour: item.hour
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

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: "#f2f2f2",
    },
    header: {
        fontSize: 24,
        fontWeight: "bold",
        margin: 15,
    },
    counterSection: {
        padding: 20,
        backgroundColor: "white",
        alignItems: "center",
        borderBottomWidth: 1,
        borderColor: "#ddd",
    },
    counterText: {
        fontSize: 18,
        fontWeight: "bold",
        marginBottom: 10,
    },
    centeredView: {
        flex: 1, 
        justifyContent: "center", 
        alignItems: "center", 
        backgroundColor: "rgba(0,0,0,0.5)"
    },
    modalView: {
        backgroundColor: "white", 
        padding: 35, 
        borderRadius: 20, 
        alignItems: "center"
    },
    modalTitle: {
        fontSize: 20, 
        fontWeight: "bold", 
        marginBottom: 15
    }
});