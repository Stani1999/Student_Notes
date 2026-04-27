import { Text, View, Pressable } from "react-native";
import { styles } from "@/styles/ListItemStyles";

type ListItemProps = {
    title: string;
    description: string;
    location: string;
    hour: string;
    date: string;
    category: string;
    speaker: string;
    isHighlighted: boolean;
    isWorkshop?: boolean;
    onPress?: () => void;
};

export default function ListItem({ title, description, location, hour, date, category, speaker, isHighlighted, isWorkshop, onPress }: ListItemProps) {
    return (
        <Pressable
            onPress={onPress}
            style={({ pressed }) => [
                styles.container,
                isHighlighted ? styles.important : styles.default,
                isWorkshop && { backgroundColor: "#fff3cd" },
                pressed && styles.active,
                { opacity: pressed ? 0.7 : 1 }
            ]}>
            <View>
                <Text style={styles.title}>{title}</Text>
                <Text style={styles.description}>{description}</Text>
                <Text style={styles.location}>{location}</Text>
                <Text style={styles.location}>{hour}</Text>
                <Text style={styles.location}>{date}</Text>
                <Text style={styles.location}>{category}</Text>
                <Text style={styles.location}>{speaker}</Text>
            </View>
        </Pressable>
    );
}