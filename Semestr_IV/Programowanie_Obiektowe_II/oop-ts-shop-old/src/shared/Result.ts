export type Result<T, E> =
    | { success: true; data: T }
    | { success: false; error: E };

export function ok<T>(data: T): Result<T, never> {
    return { success: true, data };
}

export function fail<E>(error: E): Result<never, E> {
    return { success: false, error };
}