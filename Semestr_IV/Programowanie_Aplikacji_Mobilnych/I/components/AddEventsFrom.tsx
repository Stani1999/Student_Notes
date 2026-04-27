import { useState } from "react";
import { View, TextInput, Button, StyleSheet, Alert } from "react-native";
import { Event } from "@/types/Event"; 

type AddEventFormProps = {
    onAddEvent: (newEvent: Omit<Event, "id">) => void;
};

export default function AddEventForm({ onAddEvent }: AddEventFormProps) {
    const [title, setTitle] = useState("");
    const [description, setDescription] = useState("");
    const [location, setLocation] = useState("");
    const [hour, setHour] = useState("");
    const [date, setDate] = useState("");
    const [category, setCategory] = useState("");
    const handleAddEvent = () => {
        if (!title || !description || !location || !hour || !date || !category) {
            Alert.alert("Error", "Please fill in all fields");
            return;
        }

        onAddEvent({
            title, 
            description, 
            location, 
            hour,
            date, 
            category 
        });

        setTitle("");
        setDescription("");
        setLocation("");
        setHour("");
        setDate("");
        setCategory("");
    };

    return (
        <View>
            <TextInput
            placeholder="Data (np. 2137.09.11)"
            value={date}
            onChangeText={setDate}
            style={styles.input}
        />

        <TextInput
        placeholder="Category"
        value={category}
        onChangeText={setCategory}
        style={styles.input}
        />

        <Button title="Add Event" onPress={handleAddEvent} />
        </View>
    );
}

const styles = StyleSheet.create({
    input: {
        borderWidth: 1,
        borderColor: "#ccc",
        borderRadius: 8,
        padding: 10,
        marginBottom: 10,
        backgroundColor: "#fff",
    },
});