import { StyleSheet } from "react-native";

export const styles = StyleSheet.create({
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