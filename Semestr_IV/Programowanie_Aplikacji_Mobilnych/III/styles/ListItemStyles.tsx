import { StyleSheet } from "react-native";

export const styles = StyleSheet.create({
    container: {
        padding: 20,
        marginVertical: 5,
        marginHorizontal: 10,
        borderRadius: 8,
        elevation: 2,
        shadowColor: "#000",
        shadowOffset: { width: 0, height: 1 },
        shadowOpacity: 0.2,
        shadowRadius: 1.41,
    },
    default: {
        backgroundColor: "#4a90e2",
    },
    important: {
        backgroundColor: "#f39c12",
    },
    active: {
        backgroundColor: "#1f4f85",
        transform: [{ scale: 0.98 }],
    },
    title: {
        color: "white",
        fontSize: 18,
        fontWeight: "bold",
    },
    description: {
        color: "white",
        fontSize: 14,
    },
    location: {
        color: "white",
        fontSize: 12,
        marginTop: 5,
        fontStyle: 'italic',
    }
});