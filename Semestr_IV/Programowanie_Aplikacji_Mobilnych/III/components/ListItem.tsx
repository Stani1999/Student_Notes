import { StyleSheet, Text, View, Pressable } from "react-native";

type ListItemProps = {
    title: string;
    description: string;
    location: string;
    isHighlighted: boolean;
    onPress?: () => void;
};

export default function ListItem({ title, description, location, isHighlighted, onPress }: ListItemProps) {
    return (
        <Pressable
            onPress={onPress}
            style={({ pressed }) => [
                styles.container,
                isHighlighted ? styles.important : styles.default,
                pressed && styles.active,
                { opacity: pressed ? 0.7 : 1 }
            ]}>
            <View>
                <Text style={styles.title}>{title}</Text>
                <Text style={styles.description}>{description}</Text>
                <Text style={styles.location}>{location}</Text>
            </View>
        </Pressable>
    );
}

const styles = StyleSheet.create({
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