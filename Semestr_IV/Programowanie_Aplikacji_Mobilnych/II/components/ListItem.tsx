import { View, Text, StyleSheet } from 'react-native';

type ListItemProps = {
    title: string;
    description: string;
    location: string;
    isHighlighted: boolean;
};

export default function ListItem({ title, description, location, isHighlighted }: ListItemProps) {
    return (
        <View style={[styles.container, isHighlighted && styles.highlighted]}>
            <Text style={styles.title}>{title}</Text>
            <Text style={styles.description}>{description}</Text>
            <Text style={styles.location}>{location}</Text>
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        padding: 15,
        borderBottomWidth: 1,
        borderBottomColor: '#ccc',
    },
    highlighted: {
        backgroundColor: '#fff9c4',
    },
    title: {
        fontSize: 18,
        fontWeight: 'bold',
    },
    description: {
        fontSize: 14,
        color: '#666',
    },
    location: {
        fontSize: 12,
        color: '#999',
        fontStyle: 'italic',
    },
});