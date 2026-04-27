import { useState } from "react";
import { View, TextInput, Button, Alert } from "react-native";
import { Event } from "@/types/Event";
import { styles } from "@/styles/InputStyle";

type AddEventFormProps = {
    onAddEvent: (event: Omit<Event, "id">) => void;
};

export default function AddEventForm({ onAddEvent }: AddEventFormProps) {
    const [title, setTitle] = useState("");
    const [description, setDescription] = useState("");
    const [hour, setHour] = useState("");
    const [location, setLocation] = useState("");
    const [date, setDate] = useState("");
    const [category, setCategory] = useState("");    
    const [speaker, setSpeaker] = useState("");

    const handleAddEvent = () => {
        if (title.length < 3) {
            Alert.alert("Blad", "Tytul musi miec co najmniej 3 znaki.");
            return;
        }

        if (!date.trim()) {
            Alert.alert("Blad", "Data nie moze byc pusta.");
            return;
        }

        if (!description || !hour || !location || !category || !speaker) {
            Alert.alert("Blad", "Wszystkie pola musza byc uzupelnione.");
            return;
        }

        onAddEvent({
            title,
            description,
            hour,
            location,
            date,
            category,
            speaker,
        });

        Alert.alert("Sukces!", "Wydarzenie zostało pomyślnie dodane.");
        handleClearForm();
    }

    const handleClearForm = () => {
        setTitle("");
        setDescription("");
        setHour("");
        setLocation("");
        setDate("");
        setCategory("");
        setSpeaker("");
    }

    return (
        <View>
            <TextInput 
                placeholder="Tytuł"
                value={title}
                onChangeText={setTitle}
                style={styles.input}
            />
            <TextInput 
                placeholder="Opis"
                value={description}
                onChangeText={setDescription}
                style={styles.input}
            />
            <TextInput 
                placeholder="Godzina"
                value={hour}
                onChangeText={setHour}
                style={styles.input}
            />
            <TextInput 
                placeholder="Lokalizacja"
                value={location}
                onChangeText={setLocation}
                style={styles.input}
            />
            <TextInput 
                placeholder="Data"
                value={date}
                onChangeText={setDate}
                style={styles.input}
            />
            <TextInput 
                placeholder="Kategoria"
                value={category}
                onChangeText={setCategory}
                style={styles.input}
            />
            <TextInput 
                placeholder="Prelegent"
                value={speaker}
                onChangeText={setSpeaker}
                style={styles.input}
            />
            <Button title="Dodaj wydarzenie" onPress={handleAddEvent} />
            <Button title="Wyczyść formularz" onPress={handleClearForm} />
        </View>
    )
}