import { Text, View } from "react-native";
import { StyleSheet } from "react-native";

type HeaderProps = {
    title: string;
};

export default function Header({ title }: HeaderProps) {
    return (
        <View style={styles.container}>
            <Text style={styles.title}>{title}</Text>
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        padding: 20,
        backgroundColor: "#4a90e2",
    },
    title: {
        color: "white",
        fontSize: 20,
        fontWeight: "bold",
    },
});